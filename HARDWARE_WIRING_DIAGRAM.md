# Real Hardware Wiring and Integration Schematic

**CRITICAL NOTICE:** This is a wiring and schematic reference document only. **No physical hardware has been assembled yet.** Do not claim "hardware demo ready" until these connections are physically soldered, mounted, and verified on a live bench.

## 1. Verified Component List and Images

*(Note: As the student, you MUST click and verify these datasheet links to ensure they match the exact part numbers you end up purchasing.)*

| Component | Part Number (Example) | Official Datasheet / Source URL | Verified Image Reference |
| :--- | :--- | :--- | :--- |
| **Microcontroller** | ESP32-WROOM-32U DevKitC | [Espressif Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-wroom-32d_esp32-wroom-32u_datasheet_en.pdf) | [Adafruit Huzzah32 as ref](https://cdn-shop.adafruit.com/970x728/3405-04.jpg) |
| **Capacitive Sensor** | TI FDC1004 Breakout | [TI FDC1004 Datasheet](https://www.ti.com/lit/ds/symlink/fdc1004.pdf) | [SparkFun SEN-13906](https://cdn.sparkfun.com/r/500-500/assets/parts/1/1/7/4/1/13906-01a.jpg) |
| **Power Manager** | TP4056 (with protection) | [NanJing TP4056 Datasheet](https://dlnmh9ip6v2uc.cloudfront.net/datasheets/Prototyping/TP4056.pdf) | [Generic TP4056 Module](https://m.media-amazon.com/images/I/71K2A2j2tPL._SL1500_.jpg) |
| **RF Analyzer** | NanoVNA V2 | [NanoVNA Spec](https://nanorfe.com/nanovna-v2.html) | [NanoVNA V2 Device](https://nanorfe.com/images/v2_2.png) |
| **Battery** | 18650 Li-ion 3.7V | [Panasonic NCR18650B Ref](https://www.batteryspace.com/prod-specs/NCR18650B.pdf) | (Standard Cell Form Factor) |

## 2. Exact Pin-Level Connections

This wiring maps the core subsystem.

### A. Power Subsystem (TP4056 to Battery & ESP32)

* **Solar Panel 5V (+)** $\rightarrow$ TP4056 **IN+**
* **Solar Panel 5V (-)** $\rightarrow$ TP4056 **IN-**
* **18650 Battery (+)** $\rightarrow$ TP4056 **B+**
* **18650 Battery (-)** $\rightarrow$ TP4056 **B-**
* **TP4056 OUT+** $\rightarrow$ ESP32 **5V/VIN** pin *(The ESP32 module's internal AMS1117 regulator drops this 3.7V-4.2V input safely to 3.3V for the ESP32 chip).*
* **TP4056 OUT-** $\rightarrow$ ESP32 **GND**

### B. Capacitive Sensor (FDC1004 to ESP32 over I2C)

* FDC1004 **VDD** $\rightarrow$ ESP32 **3V3** (Provides 3.3V logic level)
* FDC1004 **GND** $\rightarrow$ ESP32 **GND**
* FDC1004 **SDA** $\rightarrow$ ESP32 **GPIO 21** (Default I2C Data on ESP32)
* FDC1004 **SCL** $\rightarrow$ ESP32 **GPIO 22** (Default I2C Clock on ESP32)
* FDC1004 **CIN1** $\rightarrow$ Custom Interdigitated PCB (Active Electrode)
* FDC1004 **SHLD1** $\rightarrow$ Custom Interdigitated PCB (Shield/Guard Ring layer to direct electric field)

### C. NanoVNA Power Gating (Optional / Advanced)

*As noted in `HARDWARE_FEASIBILITY.md`, running the NanoVNA 24/7 drains the battery rapidly (~400mA).*

* ESP32 **GPIO 15** $\rightarrow$ Gate of an N-Channel Logic-Level MOSFET (e.g., IRLZ44N).
* NanoVNA **USB VBUS** $\rightarrow$ Switched by the MOSFET to draw from TP4056 OUT+.
* NanoVNA **USB D+ / D-** $\rightarrow$ Cannot connect directly to standard ESP32 GPIOs without a USB Host shield.
  * **FLAG / WARNING**: The NanoVNA communicates via USB CDC (Serial over USB). The stock ESP32-WROOM-32 does *not* possess hardware USB Host capabilities. To pull data from a NanoVNA, you must either: A) Use an ESP32-S2/S3 which supports USB OTG, or B) Tap directly into the NanoVNA's internal UART test pads on its PCB.

## 3. Discrepancy Cross-Check against Previous Docs

1. **ESP32 to NanoVNA Link**: The previous `HARDWARE_MODEL.md` claimed `VNA -- UART/USB --> ESP32`. As flagged above, a standard ESP32-WROOM-32 cannot natively host a USB device. **Correction**: The hardware BOM must specify updating to an **ESP32-S3** dev board, which has native USB Host (OTG), otherwise you must hack the NanoVNA case open and solder to its internal UART lines.
2. **NanoVNA Power Draw**: The previous plan proposed waking the NanoVNA via MOSFET. Drawing an instantaneous 400mA rush from the TP4056 OUT+ might trigger a voltage sag, restarting the ESP32. **Correction**: A large electrolytic capacitor (e.g., 1000uF) must be added across the ESP32 5V/GND pins to buffer the inrush current when the NanoVNA boots.
