import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.eda import (
    summarization, missing_values, univariate, 
    bivariate, outlier_detection, visualizations
)

def main():
    df = summarization.load_data("data/insurance_data.txt")
    summarization.describe_data(df)
    summarization.check_data_types(df)
    missing_values.check_missing(df)
    univariate.plot_distributions(df)
    bivariate.plot_relationships(df)
    outlier_detection.detect_outliers(df)
    visualizations.create_key_insight_plots(df)

if __name__ == "__main__":
    main()
