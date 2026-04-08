import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
import os

def prepare_and_analyze(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Error: The file {file_path} was not found.")

    print(f"--- Loading data from {file_path} ---")
    df = pd.read_excel(file_path)
    
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    df['Month'] = df['Date'].dt.month
    df['DayOfWeek'] = df['Date'].dt.dayofweek

    le = LabelEncoder()
    df['Region_enc'] = le.fit_transform(df['Region'])
    df['Type_enc'] = le.fit_transform(df['Customer_Type'])

    features = ['Consumption_kWh', 'Avg_Last_3_Months', 'Deviation_%', 
                'Month', 'DayOfWeek', 'Region_enc', 'Type_enc']
    X = df[features]
    
    print("--- Training Isolation Forest Model ---")
    model = IsolationForest(contamination=0.096, random_state=42)
    df['Anomaly'] = model.fit_predict(X)
    
    df['Status'] = df['Anomaly'].map({1: 'Normal', -1: 'Suspicious'})
    df['Score'] = model.score_samples(X).round(3)
    
    return df