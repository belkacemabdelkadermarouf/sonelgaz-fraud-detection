Electrical Fraud Detection & Anomaly Analysis System
Author: Belakcem Abdelakder Marouf

Project: Intelligent system for classifying and predicting fraudulent consumption patterns in electrical distribution networks.

Table of Contents
Overview

Key Features

Project Structure

Installation

Usage

Contribution

License

Overview
This project is designed to detect Non-Technical Losses (NTL)—specifically electricity theft and meter tampering—within the regional grid. By utilizing unsupervised machine learning, the system identifies consumption profiles that deviate significantly from historical norms, allowing utility providers like Sonelgaz to prioritize physical audits and improve network stability.

Key Features
✅ Fraud Classification: Automatically flags profiles as "Normal" or "Suspicious" based on consumption-to-deviation ratios.

✅ Predictive ML Modeling: Employs the Isolation Forest algorithm to assign anomaly scores and predict high-risk accounts.

✅ Regional Analytics: Visualizes fraud hotspots across different districts (Ghriss, Sig, Tighennif, etc.).

✅ Interactive Dashboards: Generates a professional Plotly-based report for decision-makers.

Project Structure
Plaintext
fraud_detection_project/
├── src/
│   ├── main.py                # Main system orchestrator
│   ├── visualization.py       # Professional dashboard generation logic
│   └── analyzers/
│       └── fraud_detector.py  # ML Anomaly Detection engine
├── data/
│   ├── sonelgaz_mascara_data.xlsx  # Regional consumption dataset
│   ├── fraud_classified.csv        # Output: Categorized anomalies
│   └── risk_predictions.csv        # Output: High-risk future targets
├── reports/                   # Interactive HTML dashboards (Excluded from Git)
├── requirements.txt           # Project dependencies
└── .gitignore                 # Prevents large HTML/data files from cluttering the repo
Installation
Clone the repository:

Bash
git clone https://github.com/your-username/fraud_detection_project.git
Set up the Python Environment:

Bash
# Create a virtual environment
python -m venv venv

# Activate it (Windows)
venv\Scripts\activate

# Activate it (Mac/Linux)
source venv/bin/activate
Install Dependencies:

Bash
pip install -r requirements.txt
Usage
Run the Detection System:

Bash
python src/main.py
Access the Results:

Visual Report: Open reports/fraud_dashboard.html in any web browser to see the interactive charts.

Data Logs: Review data/fraud_classified.csv for a full list of suspicious Customer IDs.

Contribution
Contributions are welcome! If you have ideas to improve the detection accuracy:

Fork this repository.

Create a branch for your feature (git checkout -b feature/NewAlgorithm).

Submit a Pull Request.

