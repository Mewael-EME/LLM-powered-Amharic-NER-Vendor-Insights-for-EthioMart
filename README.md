# EthioMart Named Entity Recognition & Vendor Analytics

## Project Overview

This project focuses on extracting meaningful vendor-related entities from Ethiopian Telegram channels using state-of-the-art Named Entity Recognition (NER) models. The goal is to develop a robust, scalable, and interpretable system to analyze vendor activity and engagement, enabling EthioMart to offer micro-lending to promising vendors.

---

## Features

- **NER Model Fine-Tuning:** Fine-tune transformer-based models (XLM-Roberta, mBERT, DistilBERT) for Amharic and multilingual entity extraction.
- **End-to-End Data Pipeline:** Seamlessly ingest Telegram channel data from multiple sources, preprocess Amharic text (normalization, cleaning), and prepare structured datasets for training.
- **Model Comparison & Selection:** Evaluate multiple models based on accuracy, inference speed, and robustness; apply interpretability methods to explain model decisions.
- **Vendor Scorecard Analytics:** Combine extracted entities with metadata (views, timestamps) to calculate key performance metrics and generate a lending score for each vendor.
- **Interpretability Tools:** Use SHAP and LIME to ensure transparency and trust in the model's predictions.
- **Modular, Reproducible Codebase:** Clear organization, comprehensive documentation, and easy-to-follow setup instructions.

---

## Repository Structure

├── notebooks/
│ ├── task_1_data_preprocessing.ipynb
│ ├── task_4_model_comparison.ipynb
│ ├── task_5_model_interpretability.ipynb
│ ├── task_6_vendor_scorecard.ipynb
│
├── src/
│ ├── data_loader.py
│ ├── data_cleaning.py
│ ├── train_utils.py
│ ├── ner_model.py
│ ├── model_comparison.py
│ ├── interpretability.py
│ ├── vendor_scorecard.py
│
├── data/ # Raw and processed datasets (ignored in git)
├── ner-model/ # Fine-tuned models (ignored in git)
├── results/ # Model checkpoints, logs (ignored in git)
├── .gitignore
├── requirements.txt
├── train_hf_ner.py # Training script for NER models
├── README.md
└── ...


---

## Setup Instructions

### Prerequisites

- Python 3.8+
- Git
- Virtual environment tool (e.g., `venv` or `conda`)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/EthioMart-NER-Vendor-Analytics.git
cd EthioMart-NER-Vendor-Analytics

2. Create and activate a virtual environment:

python -m venv env
source env/bin/activate   # Linux/MacOS
env\Scripts\activate      # Windows

3. Install required packages:
pip install -r requirements.txt

Usage Guide
1. Data Preprocessing and Ingestion

    Use notebooks/task_1_data_preprocessing.ipynb or src/data_loader.py to preprocess raw Telegram posts.

    Normalize Amharic text to clean and prepare datasets for training.

    Supports ingestion from multiple Telegram channels.

2. Model Fine-Tuning

    Train NER models using train_hf_ner.py.

    Supports multiple transformer models (XLM-Roberta, mBERT, DistilBERT).

    Configure training parameters (learning rate, epochs, batch size) in the script.

    Save fine-tuned models for later use.

3. Model Comparison and Interpretability

    Evaluate different models via notebooks/task_4_model_comparison.ipynb and src/model_comparison.py.

    Compare accuracy, F1 scores, inference time.

    Interpret model predictions using SHAP and LIME (notebooks/task_5_model_interpretability.ipynb and src/interpretability.py).

4. Vendor Analytics & Lending Score

    Analyze vendor activity and engagement combining NER output and Telegram metadata.

    Calculate posting frequency, average views, top posts, average price points.

    Generate a final lending score to prioritize vendors.

    See notebooks/task_6_vendor_scorecard.ipynb and src/vendor_scorecard.py.

Performance Metrics
| Task                           | Model / Method        | Score / Metric                |
| ------------------------------ | --------------------- | ----------------------------- |
| Fine-Tuned NER Model           | XLM-Roberta           | F1-score: 0.86                |
|                                | mBERT                 | F1-score: 0.82                |
|                                | DistilBERT            | F1-score: 0.80                |
| Model Interpretability         | SHAP / LIME           | Visual explanations provided  |
| Vendor Analytics Lending Score | Custom Weighted Score | Based on views & posting freq |

Project Highlights

    Robust NER Fine-tuning: Uses Hugging Face Transformers with proper token-label alignment.

    Multi-channel Pipeline: Processes data from 5+ Telegram channels, handling Amharic normalization.

    Comprehensive Model Evaluation: Side-by-side comparison with clear performance metrics and interpretability.

    Actionable Vendor Scorecard: Data-driven lending score to support EthioMart's micro-lending decisions.

    Well-Documented and Modular Code: Clean architecture, extensive comments, and reproducible workflows.

Notes & Recommendations

    Ensure your .gitignore excludes large model files (ner-model/, results/, data/) to keep repo clean.

    Always run scripts/notebooks in a fresh virtual environment.

    Customize hyperparameters based on dataset size and compute resources.

    Use GPU acceleration when available to speed up training.

    Extend interpretability analyses to further improve model trustworthiness.

