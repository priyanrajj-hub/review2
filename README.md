# GlobalPlantHealth Hardware Node

This companion repository serves as the ground-truth node architecture for the **Solar Plant Health Monitoring (AGRISENSE)** system:

- **Satellite Dashboard repo:** <https://github.com/priyanrajj-hub/smart-plant-health-monitoring-using-solar-images>

## Architecture

The node physically measures micro-climate and physiological data mapped to the satellite's macroscopic coordinates:

- **MCU:** ESP32-S3 (low power sleep modes, BLE)
- **Dielectric Moisture:** FDC1004 (Leaf Capacitance sensing)
- **Acoustic:** INMP441 (Xylem Cavitation Emissions)
- **Microclimate:** DS18B20 & BME280

These sensors feed the `w_C` (capacitive) and `w_A` (acoustic) base inputs to the MOONLIGHT Bayesian fusion algorithm deployed on the software counterpart.
