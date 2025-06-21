def write_conll(messages, tokenizer, labeler, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for message in messages:
            tokens = tokenizer(message)
            labeled_tokens = labeler(tokens)
            for token, label in labeled_tokens:
                f.write(f"{token} {label}\n")
            f.write("\n")
