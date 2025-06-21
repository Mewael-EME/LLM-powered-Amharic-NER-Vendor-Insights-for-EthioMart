import re

def tokenize_amharic(text):
    # Basic tokenizer: splits by whitespace and keeps punctuation
    return re.findall(r'\w+|[^\w\s]', text, re.UNICODE)

def get_entity_label(tokens):
    """
    Labels tokens with CoNLL-style tags based on simple rule-based heuristics.
    Returns a list of (token, label) tuples.
    """
    labels = []
    prev_entity = "O"

    for i, token in enumerate(tokens):
        # Price entity
        if token.isdigit() or token == "ብር" or "ዋጋ" in token or "በ" == token:
            entity = "PRICE"
        elif token in ["አዲስ", "ቦሌ", "ልደታ", "ቤት", "ከተማ"]:
            entity = "LOC"
        elif token in ["ሻይ", "አልጋ", "ቡና", "ቁሳቁስ", "መጠጥ"]:
            entity = "Product"
        else:
            entity = "O"

        if entity == "O":
            label = "O"
        elif entity == prev_entity:
            label = f"I-{entity}"
        else:
            label = f"B-{entity}"
        
        labels.append((token, label))
        prev_entity = entity

    return labels
