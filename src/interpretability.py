import shap
import lime
import lime.lime_text
import numpy as np
import torch
from transformers import AutoTokenizer

class NERExplainer:
    def __init__(self, model, tokenizer_name):
        self.model = model
        self.tokenizer = AutoTokenizer.from_pretrained(tokenizer_name)
        self.model.eval()

    def predict_proba(self, texts):
        encodings = self.tokenizer(texts, return_tensors='pt', padding=True, truncation=True)
        with torch.no_grad():
            outputs = self.model(**encodings)
        probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
        return probs.detach().cpu().numpy()

    def explain_with_lime(self, sample_text):
        explainer = lime.lime_text.LimeTextExplainer(class_names=["O", "B-PER", "I-PER", "B-LOC", "I-LOC", "B-ORG", "I-ORG"])
        return explainer.explain_instance(sample_text, self.predict_proba, num_features=6)

    def explain_with_shap(self, text_list):
        explainer = shap.Explainer(self.predict_proba, self.tokenizer)
        shap_values = explainer(text_list)
        return shap_values