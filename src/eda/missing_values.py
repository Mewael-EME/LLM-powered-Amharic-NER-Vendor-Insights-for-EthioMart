# src/eda/missing_values.py
import pandas as pd

def check_missing(df):
    missing_report = pd.DataFrame({
        'Column': df.columns,
        'MissingCount': df.isnull().sum(),
        'MissingPercent': (df.isnull().sum() / len(df)) * 100
    })
    print("Missing Values Report:")
    print(missing_report)
