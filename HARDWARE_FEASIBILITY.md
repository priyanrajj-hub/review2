# Hardware Feasibility Report & BOM (<$150)

This report details the proposed hardware architecture for low-cost ($<150), field-deployable microwave/dielectric leaf sensing.

## 1. Primary Bill of Materials (BOM)

| Component | Purpose / Description | Estimated Cost (USD) |
| :--- | :--- | :--- |
| **NanoVNA V2 (or H4)** | Generates and measures S-parameters (50kHz - 3GHz/15GHz). | $50.00 - $70.00 |
| **ESP32-WROOM-32U DevKit** | Microcontroller for automation, TinyML inference, and WiFi/BLE data logging. | $8.00 |
| **Sensor Interface (Interdigitated Cu)** | Custom PCB for capacitive sensing/resonator interface. | $5.00 |
| **DHT22 / BME280** | Temperature and Rel Hum sensor for environmental cross-sensitivity compensation. | $6.00 |
| **Solar Power Array & Battery** | 5V 1W Solar panel + TP4056 Lipo charger + 18650 3.7V 3000mAh. | $15.00 |
| **Conformal Coating & Enclosure** | MG Chemicals Silicone Conformal Coating, Weatherproof PG7 glands, IP67 ABS Box. | $25.00 |
| **Miscellaneous** | SMA cables, clamping mechanism (e.g., 3D printed soft TPU). | $10.00 |
| **Total Estimated Cost:** | | **~ $139.00** |

*(Alternative: Replace NanoVNA with TI LDC1614 EVM for pure capacitive testing ~$30, which reduces total cost to well under $100).*

## 2. Addressing Challenges

### Electrode Degradation and Weatherproofing

- **Issue**: Exposed copper electrodes oxidize, and moisture (dew/rain) causes massive parasitic capacitance that ruins measurements.
- **Solution**: The sensing electrodes must be spin-coated or brushed with a thin, controlled layer of **Parylene-C** or a high-grade silicone conformal coating. This isolates the conductive contacts from direct water exposure while allowing the electric field to penetrate the leaf tissue. The shift in baseline capacitance due to the coating must be recorded and calibrated out in firmware.

### Attachment Modality: Tomato vs. Coconut

- **Tomato/Chilli (Soft, fragile)**: A lightweight, spring-loaded 3D-printed TPU (flexible) clamp. It must apply constant, gentle pressure (e.g., < 0.5 N) without crushing the xylem/phloem.
- **Coconut (Rigid, large, curved)**: Traditional clamps snap or slip. We recommend a *proximity-based conformal backing* (using a velcro strap wrap around the frond) where the dielectric sensor is pressed flush against the flat underside of the frond, minimizing mechanical shear stress on the plant.

### Temperature Cross-Sensitivity

- **Issue**: The dielectric constant of water itself changes by roughly -0.4% per °C. As field temperatures range from 15°C to 40°C, the sensor will drift dramatically even if LWC is constant.
- **Solution**: The BOM includes a BME280. The ML pipeline (Random Forest) will ingest Temperature and ambient RH as direct feature inputs alongside the impedance spectrum. The ML model will inherently learn to compensate for thermal drift.

### Power & Field Deployment

- **Design**: The ESP32 consumes roughly 150-240 mA when active and ~10 µA in deep sleep. The NanoVNA draws ~400 mA.
- **Duty Cycling**: The ESP32 will wake up every 30 minutes, switch a MOSFET to power on the NanoVNA, wait 5 seconds for calibration/stabilization, pull the sweeping data over UART/USB, log it to SD/WiFi, and return the system to deep sleep.
- **Sustainability**: An 18650 cell (3000mAh) provides roughly ~7 days of operation natively. Paired with a 5V/1W solar panel, the system can run indefinitely unattended.
