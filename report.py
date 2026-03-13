from reportlab.pdfgen import canvas
from reportlab.platypus import Image
import os

REPORT_FOLDER = "reports"
os.makedirs(REPORT_FOLDER, exist_ok=True)

def create_report(summary, chart_paths=[]):
    file_path = os.path.join(REPORT_FOLDER, "report.pdf")
    c = canvas.Canvas(file_path)
    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(200, 800, "AutoReport AI")
    
    c.setFont("Helvetica", 12)
    y = 750
    for key, value in summary.items():
        c.drawString(50, y, f"{key}: {value}")
        y -= 20
    
    # Add charts
    for chart in chart_paths:
        y -= 200
        c.drawImage(chart, 50, y, width=500, height=150)
    
    c.save()
    return file_path