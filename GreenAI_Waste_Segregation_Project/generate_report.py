# generate_report.py
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_report(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 750, "Waste Segregation Report")
    c.drawString(100, 730, "This is a generated report from the Green AI system.")
    c.save()

create_report("waste_report.pdf")
