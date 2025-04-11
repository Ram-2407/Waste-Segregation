# Enhanced Streamlit App
import streamlit as st
from PIL import Image
import pandas as pd
import io
from image_classifier import classify_image
from iot_simulation import generate_sensor_data
import joblib
import os

st.set_page_config(page_title="Green AI Waste Segregation", layout="centered")
st.title("Green AI Waste Segregation System")

# Image Upload
st.header("📸 Upload or Capture Waste Image")
img_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if img_file is not None:
    image_data = Image.open(img_file)
    st.image(image_data, caption="Uploaded Image", use_column_width=True)
    label, confidence = classify_image(image_data)
    st.success(f"Image classified as: **{label}** with confidence {confidence:.2f}")

# Simulated IoT Data
st.header("📊 Simulated IoT Sensor Data")
sensor_data = generate_sensor_data()
st.json(sensor_data)

# Generate Report
if st.button("📄 Generate PDF Report"):
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter

    report_path = "enhanced_waste_report.pdf"
    c = canvas.Canvas(report_path, pagesize=letter)
    c.drawString(100, 750, "Enhanced Waste Segregation Report")
    c.drawString(100, 730, f"Predicted Waste Type (Image): {label} ({confidence:.2f})")
    c.drawString(100, 710, f"Sensor Data: {sensor_data}")
    c.save()
    with open(report_path, "rb") as f:
        st.download_button("Download Report", f, file_name="waste_report.pdf")
