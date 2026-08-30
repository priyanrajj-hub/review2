import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import os

def generate_synthetic_data(num_samples=200):
    """
    Simulates NanoVNA S11 resonance data and LDC capacitance data for Tomato, Chilli, and Coconut leaves.
    """
    np.random.seed(42)
    
    # Simulate Ground Truth Leaf Water Content (LWC) ranging from 40% to 90%
    lwc_true = np.random.uniform(40, 90, num_samples)
    
    # 1. Resonant Frequency (GHz) - inversely correlated with LWC
    # As LWC goes up, dielectric constant goes up, resonant frequency goes down
    res_freq = 2.4 - 0.005 * lwc_true + np.random.normal(0, 0.05, num_samples)
    
    # 2. Capacitance (pF) - positively correlated with LWC
    capacitance = 10 + 0.5 * lwc_true + np.random.normal(0, 1.5, num_samples)
    
    # 3. Temperature cross-sensitivity (15C to 35C)
    temperature = np.random.uniform(15, 35, num_samples)
    # Capacitance drifts with temp
    capacitance += (temperature - 25) * 0.1
    
    # Plant Type (0: Tomato, 1: Chilli, 2: Coconut)
    plant_type = np.random.randint(0, 3, num_samples)
    
    # Coconut leaves have a much lower baseline capacitance due to waxy cuticle
    capacitance[plant_type == 2] -= 15
    # Tomato leaves have a higher baseline capacitance
    capacitance[plant_type == 0] += 5
    
    X = np.column_stack((res_freq, capacitance, temperature, plant_type))
    y = lwc_true
    
    return X, y

def run_simulation_model():
    print("Generating Synthetic Data (60% Simulation Model)...")
    X, y = generate_synthetic_data()
    
    print("Splitting Data and Training Random Forest Regressor...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestRegressor(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print(f"Simulation Results: MSE = {mse:.2f}, R2 = {r2:.2f}")
    
    # Visualization
    plt.figure(figsize=(8, 6))
    plt.scatter(y_test, y_pred, alpha=0.7, color='b')
    plt.plot([40, 90], [40, 90], 'r--', lw=2)
    plt.xlabel("True Leaf Water Content (%)")
    plt.ylabel("Predicted Leaf Water Content (%)")
    plt.title("Simulation Model: Microwave Dielectric Sensing of LWC")
    plt.grid(True)
    
    os.makedirs("results", exist_ok=True)
    plt.savefig("results/simulation_accuracy.png")
    print("Saved simulation plot to results/simulation_accuracy.png")

if __name__ == "__main__":
    run_simulation_model()
