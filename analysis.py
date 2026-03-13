import pandas as pd

def analyze_data(df):
    summary = {
        "Total Rows": len(df),
        "Total Columns": len(df.columns),
        "Missing Values": df.isnull().sum().to_dict(),
        "Statistics": df.describe().to_dict()
    }
    return summary