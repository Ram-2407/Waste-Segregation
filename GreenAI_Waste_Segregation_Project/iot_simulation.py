# iot_simulation.py
import random

def generate_sensor_data():
    return {
        'weight': round(random.uniform(0.1, 5.0), 2),  # in kg
        'moisture': round(random.uniform(10.0, 90.0), 2),  # in %
        'proximity': round(random.uniform(1.0, 30.0), 2)  # in cm
    }
