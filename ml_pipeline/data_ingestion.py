import pandas as pd
import numpy as np
import os
import glob

def load_nanovna_s1P(filepath):
    """
    Loads NanoVNA Touchstone (.s1p) files.
    Returns frequencies and complex S11 parameters.
    """
    try:
        # skiprows typically 5 to skip header of Touchstone format
        data = pd.read_csv(filepath, sep='\s+', skiprows=5, header=None)
        freqs = data[0].values
        # Re/Im format or Mag/Angle format handling
        # Assuming Re/Im format: S11_Re = data[1], S11_Im = data[2]
        s11_complex = data[1].values + 1j * data[2].values
        return freqs, s11_complex
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None, None

def load_sensor_csv(filepath):
    """
    Loads standard capacitive/environmental logs (LDC161x or BME280).
    Expected columns: timestamp, capacitance_pF, temp_C, hum_RH, True_LWC
    """
    return pd.read_csv(filepath)

def test_ingestion():
    # Placeholder for actual testing once data is collected
    print("Ingestion pipeline loaded successfully. Waiting for collected dataset.")

if __name__ == "__main__":
    test_ingestion()
