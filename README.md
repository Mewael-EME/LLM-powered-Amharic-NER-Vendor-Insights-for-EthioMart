# Insurance Risk Analytics - Week 03

This project performs structured Exploratory Data Analysis (EDA) on an insurance dataset as part of the KAIM weekly challenge. The EDA is modularized into reusable scripts and visualized interactively in a Jupyter Notebook.

---

## 🔧 Project Structure

Insurance_risk_analytics_week_03/
├── data/
│ └── insurance_data.txt # Dataset
├── notebooks/
│ └── analysis.ipynb # Jupyter notebook with full EDA
├── scripts/
│ └── run_eda.py # Main script to execute EDA pipeline
├── src/
│ └── eda/
│ ├── summarization.py # Descriptive statistics & dtype checks
│ ├── missing_values.py # Missing value reporting
│ ├── univariate.py # Univariate plots (histograms, bars)
│ ├── bivariate.py # Correlation & scatter plots
│ └── outliers.py # Box plots for outlier detection


---

## 📌 EDA Tasks Overview

### ✅ 1. Data Overview
- Loaded and previewed the dataset.
- Computed summary statistics for numerical columns like:
  - `TotalPremium`, `TotalClaim`, etc.
- Verified data types to ensure proper classification of numerical, categorical, and date fields.

### ✅ 2. Data Quality Check
- Detected and quantified missing values across features.
- Generated a summary table with both counts and percentages of missing entries.

### ✅ 3. Univariate Analysis
- Visualized distributions of:
  - Numeric columns using histograms
  - Categorical columns using bar charts
- Plots are saved in the `task4/plots/` directory.

### ✅ 4. Bivariate & Multivariate Exploration
- Analyzed variable relationships:
  - Correlation matrix for numerical columns
  - Scatter plots of `TotalPremium` vs `TotalClaim`, colored by `ZipCode`
- Aimed to uncover associations and regional trends.

### ✅ 5. Comparative Analysis
- Compared key attributes by geography:
  - Box plots of `TotalPremium` by `CoverType` and `ZipCode`
  - Frequency distribution of `AutoMake` by region

### ✅ 6. Outlier Detection
- Identified potential outliers using box plots:
  - Focused on features such as `TotalPremium` and `TotalClaim`

### ✅ 7. Key Visual Insights
Three custom plots were created to highlight important findings:
1. **Premium-Claim Ratio** – Distribution showing relative risk levels
2. **Top AutoMakes by Region** – Popular car makes across different zip codes
3. **Monthly Premium Patterns** – Time-based trends in total premiums (if temporal data exists)

---

## 🚀 How to Use

### ▶️ Run the Notebook
```bash
jupyter notebook notebooks/analysis.ipynb

🐍 Run via Script

python scripts/run_eda.py

📦 Requirements
Install dependencies using:

pip install pandas matplotlib seaborn

Or via:

pip install -r requirements.txt

👨‍💻 Author

Mewael Mizan Tesfay
