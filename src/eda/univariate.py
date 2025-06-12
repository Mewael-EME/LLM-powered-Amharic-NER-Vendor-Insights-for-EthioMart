# src/eda/univariate.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_distributions(df):
    num_cols = df.select_dtypes(include='number').columns
    cat_cols = df.select_dtypes(exclude='number').columns

    print("\n Plotting Histograms for Numeric Columns")
    for col in num_cols:
        plt.figure(figsize=(6, 4))
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
        plt.savefig(f'plots/hist_{col}.png')
        plt.close()

    print("\n Plotting Bar Charts for Categorical Columns")
    for col in cat_cols:
        if df[col].nunique() < 15:  # Avoid clutter
            plt.figure(figsize=(6, 4))
            df[col].value_counts().plot(kind='bar')
            plt.title(f'Frequency of {col}')
            plt.savefig(f'plots/bar_{col}.png')
            plt.close()
