from transformers import AutoTokenizer, AutoModelForTokenClassification

def load_model_and_tokenizer(model_name="Davlan/bert-base-multilingual-cased-ner-hrl", num_labels=7):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name, num_labels=num_labels)
    return tokenizer, model
