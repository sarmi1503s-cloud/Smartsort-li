

# SmartSort-Li 
### AI-Powered Multi-Sensor Lithium Battery E-Waste Sorting System

SmartSort-Li is a proof-of-concept system that combines **AI-based battery detection, temperature sensing, and automatic servo sorting** to improve the safety and efficiency of lithium battery e-waste handling.

## Features

-  **AI Detection:** Identifies battery types using Roboflow.
-  **Temperature Monitoring:** Reads temperature using a DS18B20 sensor.
-  **Sensor Fusion:** Combines AI confidence and temperature to classify batteries.
-  **Automatic Sorting:** Uses an ESP32 and MG90S servo to route batteries.
-  **Python Control:** Connects AI and sensors with the physical sorting mechanism.

##  Classification Logic

| Condition | Decision | Servo |
|---|---|---|
| Battery not detected | Needs Testing | 45° |
| Temperature ≥ 45°C | Hazardous | 90° |
| AI confidence < 60% | Needs Testing | 45° |
| Otherwise | Safe | 0° |

**Physical bin positions:**
- Left → Needs Testing (45°)
- Centre → Safe (0°)
- Right → Hazardous (90°)

## Hardware

- ESP32 DevKit
- Webcam
- DS18B20 temperature sensor
- MG90S servo motor
- Breadboard and jumper wires
- Cardboard sorting bins

## Software

- Python
- Roboflow AI
- OpenCV / Computer Vision
- Arduino IDE
- ESP32 Serial Communication

## Project Files

- `fusion_main.py` – AI, temperature, sensor fusion, and ESP32 control
- `servo_test.py` – Servo testing program
- `smartsort_li.ino` – ESP32 temperature and servo code
- `requirements.txt` – Required Python libraries

 Usefulness for Elderly People

SmartSort-Li can help reduce the need for elderly people to manually handle discarded lithium batteries.

- Reduces direct contact with potentially overheated batteries.
- Helps lower the physical effort required for manual sorting.
- Supports safer waste-handling environments.
- Can assist recycling workers and community waste-management teams.

The system is designed as a **safety-oriented prototype** and does not replace certified battery safety inspection.

##  Future Improvements

- Battery damage and swelling detection
- QR / barcode-based battery information
- Automated conveyor system
- Cloud-based recycling records
- Improved AI-based hazard detection

SmartSort-Li provides several benefits:

- **Efficient Waste Management:** Improves battery waste sorting and recycling.
- **Improved Safety:** Reduces direct manual handling of potentially hazardous batteries.
- **Automation:** Reduces physical effort and repetitive sorting tasks.
- **Employment Opportunities:** Creates opportunities for disabled people to participate in e-waste management through accessible, technology-supported roles.
- **Environmental Protection:** Supports responsible battery disposal and recycling.
- **Smart City Development:** Combines AI and IoT to support safer and more sustainable cities.

SmartSort-Li aims to promote inclusive employment, safer working environments, and sustainable e-waste management.

##  Disclaimer
The 45°C temperature threshold and 60% AI confidence threshold are demonstration parameters for this proof-of-concept. They are not certified lithium battery safety limits.
