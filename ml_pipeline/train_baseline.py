import numpy as np
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import LeaveOneGroupOut
from sklearn.metrics import mean_squared_error, r2_score

def train_baseline_model(X, y, groups):
    """
    Trains a Random Forest using Leave-One-Plant-Out Cross-Validation (LOPO-CV).
    groups: An array of plant IDs, ensuring no leakage between train/test folds from the same plant.
    """
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    
    cv = LeaveOneGroupOut()
    y_true_all, y_pred_all = [], []
    
    # LOPO-CV Loop
    for train_idx, test_idx in cv.split(X, y, groups):
        X_train, y_train = X[train_idx], y[train_idx]
        X_test, y_test = X[test_idx], y[test_idx]
        
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        
        y_true_all.extend(y_test)
        y_pred_all.extend(y_pred)
        
    mse = mean_squared_error(y_true_all, y_pred_all)
    r2 = r2_score(y_true_all, y_pred_all)
    
    print(f"LOPO-CV Results:")
    print(f"MSE: {mse:.4f}")
    print(f"R2 : {r2:.4f}")
    
    # Fit final model on all data for deployment
    model.fit(X, y)
    return model

if __name__ == "__main__":
    # Dummy data for validation
    X_dummy = np.random.rand(50, 4) # 4 features
    y_dummy = X_dummy[:, 0] * 2 + np.random.normal(0, 0.1, 50) # target
    groups_dummy = np.repeat([1, 2, 3, 4, 5], 10) # 5 plants, 10 samples each
    
    print("Executing baseline training trace...")
    train_baseline_model(X_dummy, y_dummy, groups_dummy)
