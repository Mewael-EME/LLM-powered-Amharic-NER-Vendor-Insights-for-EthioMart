# src/eda/outlier_detection.py

import seaborn as sns
import matplotlib.pyplot as plt

def detect_outliers(df):
    print("\n Outlier Detection using Boxplots")
    num_cols = df.select_dtypes(include='number').columns

    for col in num_cols:
        plt.figure(figsize=(6, 4))
        sns.boxplot(x=df[col])
        plt.title(f'Boxplot of {col}')
        plt.savefig(f'task4/plots/box_{col}.png')
        plt.close()
