import matplotlib.pyplot as plt
import os

REPORT_FOLDER = "reports"
os.makedirs(REPORT_FOLDER, exist_ok=True)

def generate_chart(df, column):
    plt.figure()
    df[column].hist()
    plt.title(f"{column} Distribution")
    
    chart_path = os.path.join(REPORT_FOLDER, f"{column}_chart.png")
    plt.savefig(chart_path)
    plt.close()
    
    return chart_path