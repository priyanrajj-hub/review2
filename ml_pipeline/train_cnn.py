import tensorflow as tf
import numpy as np
import os

def create_1d_cnn(input_shape):
    """
    Create a lightweight 1D-CNN for raw S-parameter/Impedance spectra.
    """
    model = tf.keras.Sequential([
        tf.keras.layers.Conv1D(filters=16, kernel_size=5, activation='relu', input_shape=input_shape),
        tf.keras.layers.MaxPooling1D(pool_size=2),
        tf.keras.layers.Conv1D(filters=32, kernel_size=3, activation='relu'),
        tf.keras.layers.GlobalAveragePooling1D(),
        tf.keras.layers.Dense(16, activation='relu'),
        tf.keras.layers.Dense(1, activation='linear') # Regression target (LWC)
    ])
    
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

def export_to_tflite(model, export_path="model.tflite"):
    """
    Export the keras model to a TinyML compatible TFLite FlatBuffer.
    """
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    # Enable optimizations for microcontrollers
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    tflite_model = converter.convert()
    
    with open(export_path, "wb") as f:
        f.write(tflite_model)
    print(f"Model exported to {export_path} ({len(tflite_model)} bytes)")

if __name__ == "__main__":
    # Dummy spectra data (e.g. 100 frequency points per sweep, 2 channels for mag/phase)
    dummy_input = np.random.rand(10, 100, 2)
    dummy_labels = np.random.rand(10)
    
    cnn = create_1d_cnn((100, 2))
    cnn.summary()
    
    # Tiny dummy training
    cnn.fit(dummy_input, dummy_labels, epochs=1, verbose=0)
    export_to_tflite(cnn)
