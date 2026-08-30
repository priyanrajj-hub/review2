import numpy as np
from scipy.signal import find_peaks

def extract_s11_features(freqs, s11_complex):
    """
    Extract physics-based features from raw S11 spectra.
    """
    # Magnitude and Phase
    magnitude = np.abs(s11_complex)
    phase = np.angle(s11_complex)
    
    # 1. Resonant Frequency (dip in S11 magnitude)
    try:
        min_idx = np.argmin(magnitude)
        res_freq = freqs[min_idx]
        res_mag = magnitude[min_idx]
    except ValueError:
        res_freq, res_mag = np.nan, np.nan
        
    # 2. Phase shifts at specific bands (e.g., 2.4 GHz, 5 GHz approx indices)
    # Using simple mean phase for placeholder
    mean_phase = np.mean(phase)
    
    # 3. Estimated Dielectric Constant shift (heuristic based on min magnitude)
    # Epsilon_r is inversely proportional to square of resonant frequency
    # We return a normalized placeholder metric
    dielectric_heuristic = 1.0 / (res_freq**2 + 1e-9) if res_freq != np.nan else 0

    return {
        "resonant_frequency_Hz": res_freq,
        "min_s11_magnitude": res_mag,
        "mean_phase_rad": mean_phase,
        "dielectric_heuristic": dielectric_heuristic
    }

def build_feature_matrix(filepath_list):
    """
    Iterate over raw data files and construct the tabular dataset for standard ML.
    """
    # TODO: Implement loop over data_ingestion.load_nanovna_s1P()
    pass

if __name__ == "__main__":
    # Dummy data test
    dummy_freqs = np.linspace(500e6, 3e9, 100)
    dummy_s11 = np.random.normal(0, 0.1, 100) + 1j * np.random.normal(0, 0.1, 100)
    dummy_s11[50] = -0.5 + 0j # Fake dip at center
    print(extract_s11_features(dummy_freqs, dummy_s11))
