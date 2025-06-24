# src/train_utils.py

from datasets import Dataset
from transformers import PreTrainedTokenizer

def align_labels_with_tokens(sentences, labels, tokenizer: PreTrainedTokenizer, label2id: dict):
    """
    Aligns word-level entity labels to tokenized input.

    Args:
        sentences (List[List[str]]): List of tokenized sentences.
        labels (List[List[str]]): Corresponding list of labels per sentence (must be str tags).
        tokenizer (PreTrainedTokenizer): The tokenizer to use.
        label2id (Dict[str, int]): Mapping from string labels to integer IDs.

    Returns:
        Dataset: HuggingFace Dataset with tokenized input and aligned label IDs.
    """

    tokenized_inputs = tokenizer(
        sentences,
        is_split_into_words=True,
        padding=True,
        truncation=True,
        return_offsets_mapping=True
    )

    aligned_labels = []

    for i, label_seq in enumerate(labels):
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        label_ids = []
        prev_word_id = None

        for word_idx in word_ids:
            if word_idx is None:
                label_ids.append(-100)
            else:
                raw_label = label_seq[word_idx]
                if not isinstance(raw_label, str):
                    raise TypeError(f"Label '{raw_label}' is not a string. Please ensure CoNLL labels are in string format.")
                
                if word_idx != prev_word_id:
                    label_ids.append(label2id[raw_label])
                else:
                    if raw_label.startswith("B-"):
                        raw_label = raw_label.replace("B-", "I-")
                    label_ids.append(label2id[raw_label])

                prev_word_id = word_idx

        aligned_labels.append(label_ids)

    tokenized_inputs["labels"] = aligned_labels
    return Dataset.from_dict(tokenized_inputs)