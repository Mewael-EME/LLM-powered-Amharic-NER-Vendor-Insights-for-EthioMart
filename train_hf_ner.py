from transformers import Trainer, TrainingArguments
from src.data_loader import load_conll_data
from src.ner_model import load_model_and_tokenizer
from src.train_utils import align_labels_with_tokens
from sklearn.model_selection import train_test_split
import numpy as np

LABELS = ["O", "B-Product", "I-Product", "B-LOC", "I-LOC", "B-PRICE", "I-PRICE"]
label2id = {l: i for i, l in enumerate(LABELS)}
id2label = {i: l for l, i in label2id.items()}

# Load data
sentences, labels = load_conll_data("data/labeled/labeled_data.conll")
train_sentences, val_sentences, train_labels, val_labels = train_test_split(sentences, labels, test_size=0.2)

# Load model & tokenizer
tokenizer, model = load_model_and_tokenizer(model_name="xlm-roberta-base", num_labels=len(LABELS))

# Align labels
train_dataset = align_labels_with_tokens(train_sentences, train_labels, tokenizer, label2id)
val_dataset = align_labels_with_tokens(val_sentences, val_labels, tokenizer, label2id)

# Training config
training_args = TrainingArguments(
    output_dir="./results",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    weight_decay=0.01,
    save_total_limit=2,
    logging_dir="./logs",
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    tokenizer=tokenizer,
)

trainer.train()
trainer.save_model("./ner-model")
