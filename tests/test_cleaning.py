from src.data_cleaning import normalize_amharic

def test_normalize_amharic_basic():
    text = "  ዋጋ  1000 ብር  "
    assert normalize_amharic(text) == "ዋጋ 1000 ብር"
