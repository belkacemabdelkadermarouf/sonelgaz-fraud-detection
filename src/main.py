import os
import sys

# Crucial: This allows main.py to see the 'analyzers' folder correctly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from analyzers.fraud_detector import prepare_and_analyze
from visualization import create_dashboard

def main():
    print("SONELGAZ FRAUD DETECTION SYSTEM")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(script_dir, "data", "sonelgaz_mascara_consumption_dataset.xlsx")

    try:
        processed_df = prepare_and_analyze(data_path)
        
        print("Generating interactive dashboard...")
        report_file = create_dashboard(processed_df)
        
        print(f"Success! Report saved to: {report_file}")
        
    except Exception as e:
        print(f"ERROR OCCURRED: {e}")

if __name__ == "__main__":
    main()