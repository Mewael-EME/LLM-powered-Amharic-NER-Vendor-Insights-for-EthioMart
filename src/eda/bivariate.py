# src/eda/bivariate.py

import seaborn as sns
import matplotlib.pyplot as plt

def plot_relationships(df):
    print("\n Correlation Matrix")
    corr = df.corr(numeric_only=True)
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.savefig('plots/correlation_matrix.png')
    plt.close()

    if 'TotalPremium' in df.columns and 'TotalClaim' in df.columns:
        print(" Scatter plot of TotalPremium vs TotalClaim")
        plt.figure(figsize=(6, 4))
        sns.scatterplot(data=df, x='TotalPremium', y='TotalClaim', hue='ZipCode', legend=False)
        plt.title('TotalPremium vs TotalClaim by ZipCode')
        plt.savefig('plots/premium_vs_claim.png')
        plt.close()
