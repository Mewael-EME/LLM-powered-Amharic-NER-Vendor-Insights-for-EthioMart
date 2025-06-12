# src/eda/visualizations.py

import seaborn as sns
import matplotlib.pyplot as plt

def create_key_insight_plots(df):
    # Insight 1: Loss Ratio by Province
    if all(x in df.columns for x in ['TotalClaim', 'TotalPremium', 'Province']):
        df['LossRatio'] = df['TotalClaim'] / (df['TotalPremium'] + 1e-6)
        province_avg = df.groupby('Province')['LossRatio'].mean().sort_values()
        plt.figure(figsize=(10, 5))
        province_avg.plot(kind='barh', color='steelblue')
        plt.title(' Average Loss Ratio by Province')
        plt.xlabel('Loss Ratio')
        plt.savefig('plots/insight_loss_ratio_by_province.png')
        plt.close()

    # Insight 2: Claims by VehicleType and Gender
    if 'VehicleType' in df.columns and 'Gender' in df.columns:
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=df, x='VehicleType', y='TotalClaim', hue='Gender')
        plt.title(' Claim Distribution by VehicleType and Gender')
        plt.savefig('plots/insight_claim_by_vehicle_gender.png')
        plt.close()

    # Insight 3: Claim trend over time
    if 'Month' in df.columns:
        monthly = df.groupby('Month')[['TotalClaim', 'TotalPremium']].sum()
        monthly.plot(figsize=(10, 5), title=' Monthly Claims vs Premiums')
        plt.savefig('plots/insight_claims_over_time.png')
        plt.close()
