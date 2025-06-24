# src/model_comparison.py

import os
from datasets import Dataset
from transformers import (
    AutoTokenizer, AutoModelForTokenClassification,
    Trainer, TrainingArguments,
)
from sklearn.metrics import classification_report
import torch
from src.data_loader import load_conll_data
from src.train_utils import align_labels_with_tokens  # your label alignment util

# Define labels and mappings (adapt as needed)
LABELS = ['O', 'B-PER', 'I-PER', 'B-LOC', 'I-LOC', 'B-ORG', 'I-ORG']  # example
label2id = {label: i for i, label in enumerate(LABELS)}
id2label = {i: label for label, i in label2id.items()}

# Paths
DATA_PATH = "data/labeled/labeled_data.conll"  # your data file
RESULTS_DIR = "results/task_4"
os.makedirs(RESULTS_DIR, exist_ok=True)

# Load data
sentences, labels = load_conll_data(DATA_PATH)

# Split into train/val (you can replace with your own split)
split_idx = int(0.8 * len(sentences))
train_sentences, val_sentences = sentences[:split_idx], sentences[split_idx:]
train_labels, val_labels = labels[:split_idx], labels[split_idx:]

# Models to compare
models_to_try = {
    "xlm-roberta-base": "xlm-roberta-base",
    "distilbert-base-uncased": "distilbert-base-uncased",
    "bert-base-multilingual-cased": "bert-base-multilingual-cased",
}

def tokenize_and_align_labels(tokenizer, sentences, labels):
    tokenized_inputs = tokenizer(
        sentences,
        is_split_into_words=True,
        padding=True,
        truncation=True,
        return_tensors="pt"
    )
    
    aligned_labels = []
    for i, label in enumerate(labels):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        previous_word_idx = None
        label_ids = []
        for word_idx in word_ids:
            if word_idx is None:
                label_ids.append(-100)
            elif word_idx != previous_word_idx:
                label_ids.append(label2id[label[word_idx]])
            else:
                # For tokens inside a word, convert B- to I-
                current_label = label[word_idx]
                if current_label.startswith("B-"):
                    current_label = current_label.replace("B-", "I-")
                label_ids.append(label2id.get(current_label, label2id["O"]))
            previous_word_idx = word_idx
        aligned_labels.append(label_ids)
    return tokenized_inputs, aligned_labels

def compute_metrics(pred):
    predictions, labels = pred
    predictions = predictions.argmax(axis=2)

    true_labels = [[id2label[l] for l in label if l != -100] for label in labels]
    true_preds = [[id2label[p] for (p, l) in zip(prediction, label) if l != -100] for prediction, label in zip(predictions, labels)]

    report = classification_report(true_labels, true_preds, output_dict=True)
    f1_score = report['weighted avg']['f1-score']
    return {"f1": f1_score}

def run_training(model_name):
    print(f"\n\n===== Training model: {model_name} =====")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(
        model_name,
        num_labels=len(LABELS),
        id2label=id2label,
        label2id=label2id
    )
    
    # Prepare datasets
    train_tokenized, train_aligned_labels = tokenize_and_align_labels(tokenizer, train_sentences, train_labels)
    val_tokenized, val_aligned_labels = tokenize_and_align_labels(tokenizer, val_sentences, val_labels)

    train_dataset = Dataset.from_dict({
        'input_ids': train_tokenized['input_ids'],
        'attention_mask': train_tokenized['attention_mask'],
        'labels': train_aligned_labels
    })
    val_dataset = Dataset.from_dict({
        'input_ids': val_tokenized['input_ids'],
        'attention_mask': val_tokenized['attention_mask'],
        'labels': val_aligned_labels
    })

    training_args = TrainingArguments(
        output_dir=os.path.join(RESULTS_DIR, model_name.replace('/', '-')),
        evaluation_strategy="epoch",
        save_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=3,
        weight_decay=0.01,
        logging_dir='./logs',
        logging_steps=10,
        load_best_model_at_end=True,
        metric_for_best_model="f1",
        greater_is_better=True,
        save_total_limit=1,
        seed=42,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=val_dataset,
        tokenizer=tokenizer,
        compute_metrics=compute_metrics,
    )

    trainer.train()
    eval_results = trainer.evaluate()
    print(f"Evaluation results for {model_name}:", eval_results)

    return eval_results, training_args.output_dir

def main():
    all_results = {}
    for model_name in models_to_try.values():
        results, output_dir = run_training(model_name)
        all_results[model_name] = results

    print("\n\n====== SUMMARY OF ALL MODELS ======")
    for model_name, metrics in all_results.items():
        print(f"Model: {model_name} - F1 Score: {metrics['eval_f1']:.4f}")

if __name__ == "__main__":
    main()
