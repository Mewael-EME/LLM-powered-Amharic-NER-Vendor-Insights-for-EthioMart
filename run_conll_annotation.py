import json
from src.annotation_utils import tokenize_amharic, get_entity_label
from src.conll_writer import write_conll

# === Load processed messages from data/processed/messages.json ===
def load_messages(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return [item["message"] for item in data if "message" in item]

# === Run annotation ===
if __name__ == "__main__":
    input_json = "data/processed/ethio_brand_collection.json"
    output_conll = "data/labeled/labeled_data.conll"  

    messages = load_messages(input_json)[:50]  
    write_conll(
        messages=messages,
        output_path=output_conll,
        tokenizer=tokenize_amharic,
        labeler=get_entity_label
    )

    print(f"✅ CoNLL annotation saved to: {output_conll}")
