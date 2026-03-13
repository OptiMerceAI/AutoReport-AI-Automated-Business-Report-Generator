from fastapi import APIRouter, UploadFile, Form
from fastapi.responses import FileResponse
import os
import pandas as pd
from app.analysis import analyze_data
from app.charts import generate_chart
from app.report import create_report

router = APIRouter()

UPLOAD_FOLDER = "uploads"
REPORT_FOLDER = "reports"

# Make sure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

@router.post("/upload")
async def upload_file(file: UploadFile):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    
    # Save uploaded CSV
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    df = pd.read_csv(file_path)
    
    summary = analyze_data(df)
    
    # Generate charts for first 2 numeric columns
    numeric_cols = df.select_dtypes(include='number').columns[:2]
    chart_paths = []
    for col in numeric_cols:
        chart_paths.append(generate_chart(df, col))
    
    # Generate PDF report
    report_file = create_report(summary, chart_paths)
    
    return FileResponse(report_file, media_type="application/pdf", filename="report.pdf")