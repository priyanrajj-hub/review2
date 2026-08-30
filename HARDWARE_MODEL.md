# Hardware Model (60% Development)

## 1. System Block Diagram

The following Mermaid diagram outlines the completed hardware schematic required for the cross-morphology capacitive leaf sensor.

```mermaid
graph TD
    subgraph Power Management
        Batt[18650 Li-ion 3.7V] --> TP4056[TP4056 Charging IC]
        Solar[5V 1W Solar Panel] --> TP4056
        TP4056 --> Boost[3.3V / 5V LDO Regulators]
    end

    subgraph Core Processing
        Boost --> ESP32[ESP32-WROOM-32U Microcontroller]
        ESP32 --> SD[MicroSD Card Logging]
    end

    subgraph Sensing Elements
        Boost --> VNA[NanoVNA V2 / S-Parameter Sweep]
        Boost --> BME280[BME280 Temp/Humidity]
        VNA -- Coax SMA --> PCB[Encapsulated Interdigitated PCB]
        BME280 -- I2C --> ESP32
        VNA -- UART/USB --> ESP32
    end
    
    subgraph Target Plant
        PCB -. Dielectric Electric Field .-> Leaf[Target Leaf: Chilli/Tomato/Coconut]
    end
```

## 2. Enclosure and Weatherproofing Implementation

- **PCB Design**: We have modeled standard interdigitated copper trace layouts using KiCad. The traces are 2mm wide with a 0.5mm gap, operating primarily in the fringing electric field regime.
- **Parylene-C Coating**: The copper acts as the conductive plate, the Parylene acts as a rigid series dielectric, and the leaf acts as the variable dielectric.
- **Mount**: The 3D model for the clamp (chilli/tomato) utilizes soft TPU material. The 60% completion represents the functional wiring diagram and ESP32 power-switching code (turning the VNA on via MOSFET to save battery).
