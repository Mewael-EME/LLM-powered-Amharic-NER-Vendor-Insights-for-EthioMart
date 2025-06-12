# src/eda/missing_values.py

def check_missing(df):
    print("\n Missing Values Report:")
    missing = df.isnull().sum()
    missing_percent = (missing / len(df)) * 100
    missing_report = pd.DataFrame({
        'Missing Values': missing,
        'Percent': missing_percent
    })
    print(missing_report[missing_report['Missing Values'] > 0])
