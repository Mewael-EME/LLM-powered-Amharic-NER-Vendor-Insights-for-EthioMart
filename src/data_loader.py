def write_conll(messages, tokenizer, labeler, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for message in messages:
            tokens = tokenizer(message)
            labeled_tokens = labeler(tokens)
            for token, label in labeled_tokens:
                f.write(f"{token} {label}\n")
            f.write("\n")
def load_conll_data(filepath):
    sentences, labels = [], []
    sentence, label_seq = [], []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                if sentence:
                    sentences.append(sentence)
                    labels.append(label_seq)
                    sentence, label_seq = [], []
            else:
                if len(line.split()) == 2:
                    token, tag = line.split()
                    sentence.append(token)
                    label_seq.append(tag)
    return sentences, labels