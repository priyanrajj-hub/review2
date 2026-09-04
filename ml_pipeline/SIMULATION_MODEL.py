import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import os

def generate_synthetic_data(num_samples=200):
    """
    WARNING: THIS IS SIMULATED DATA FOR PIPELINE VALIDATION ONLY.
    NOT YET VALIDATED AGAINST HARDWARE.
    Simulates NanoVNA S11 resonance data and LDC capacitance data for Tomato, Chilli, and Coconut leaves.
    """
    np.random.seed(42)
    
    lwc_true = np.random.uniform(40, 90, num_samples)
    res_freq = 2.4 - 0.005 * lwc_true + np.random.normal(0, 0.05, num_samples)
    capacitance = 10 + 0.5 * lwc_true + np.random.normal(0, 1.5, num_samples)
    temperature = np.random.uniform(15, 35, num_samples)
    capacitance += (temperature - 25) * 0.1
    plant_type = np.random.randint(0, 3, num_samples)
    
    capacitance[plant_type == 2] -= 15 # Coconut
    capacitance[plant_type == 0] += 5  # Tomato
    
    X = np.column_stack((res_freq, capacitance, temperature, plant_type))
    y = lwc_true
    
    return X, y

def run_simulation_model():
    print("Generating Synthetic Data (60% Simulation Model)...")
    print("STATUS: SIMULATED â€” not yet validated against hardware.")
    X, y = generate_synthetic_data()
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Simulation Results: MSE = {mse:.2f}, R2 = {r2:.2f}")
    
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.7, color='b')
    plt.plot([40, 90], [40, 90], 'r--', lw=2)
    plt.xlabel("True Leaf Water Content (%)")
    plt.ylabel("Predicted Leaf Water Content (%)")
    plt.title("SIMULATED — not yet validated against hardware")
    plt.figtext(0.5, 0.01, "SIMULATED — not yet validated against hardware", ha="center", color="red", fontweight="bold")
    
    # Add watermark to prevent misrepresentation
    plt.text(45, 85, "SIMULATED DATA\nPending Physical Validation", color='red', fontsize=12, fontweight='bold', alpha=0.5)

    plt.grid(True)
    
    os.makedirs("results", exist_ok=True)
    plt.savefig("results/simulation_accuracy.png")
    print("Saved simulation plot to results/simulation_accuracy.png")

if __name__ == "__main__":
    run_simulation_model()
