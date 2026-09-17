from inference_sdk import InferenceHTTPClient, InferenceConfiguration
import serial
import time
print("========================================")
print("       SmartSort-Li AI FUSION")
print("========================================")
PORT = "COM7"
BAUD_RATE = 115200

print("Connecting to ESP32...")

esp32 = serial.Serial(
    PORT,
    BAUD_RATE,
    timeout=1
)
time.sleep(2)

print("ESP32 connected")

print("Reading temperature from DS18B20...")

temperature = None

start_time = time.time()

while time.time() - start_time < 10:

    if esp32.in_waiting > 0:

        line = esp32.readline().decode(
            errors="ignore"
        ).strip()

        print("ESP32:", line)

        if line.startswith("TEMP:"):

            try:
                temperature = float(
                    line.replace("TEMP:", "").strip()
                )

                break

            except ValueError:
                pass

if temperature is None:

    print("ERROR: Temperature not received from ESP32.")

    esp32.close()

    exit()

print(f"Real Temperature: {temperature:.1f} °C")

API_KEY = os.getenv("ROBOFLOW_API_KEY")

client = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key=API_KEY
).configure(
    InferenceConfiguration(
        api_key_transport="header"
    )
)

image_path = "battery_test.jpg"

print()
print("Running AI detection...")

result = client.run_workflow(
    workspace_name="sarmila-0e2re",
    workflow_id="battery-detection-vbattery-detection-sszwf-cr4yd-1-yolo11n-t1-logic",
    images={
        "image": image_path
    },
    use_cache=True
)

predictions = result[0]["predictions"]["predictions"]

battery_detected = False
battery_type = "None"
ai_confidence = 0.0

if predictions:

    best_prediction = max(
        predictions,
        key=lambda prediction: prediction["confidence"]
    )

    battery_detected = True

    battery_type = best_prediction["class"]

    ai_confidence = (
        best_prediction["confidence"] * 100

print()
print("----------------------------------------")
print("           SENSOR + AI DATA")
print("----------------------------------------")

print(f"Battery Type : {battery_type}")
print(f"AI Confidence: {ai_confidence:.2f}%")
print(f"Temperature  : {temperature:.1f} °C")

print()
print("========================================")
print("             FUSION DECISION")
print("========================================")


if not battery_detected:

    decision = "NEEDS TESTING"
    command = "TEST"


elif temperature >= 45:

    decision = "HAZARDOUS"
    command = "HAZARD"


elif ai_confidence < 60:

    decision = "NEEDS TESTING"
    command = "TEST"

else:

    decision = "SAFE"
    command = "SAFE"


print(f"Decision: {decision}")


print()
print("Sending command to ESP32...")

esp32.write(
    (command + "\n").encode()
)

esp32.flush()

print(f"Sent to ESP32: {command}")


time.sleep(2)

while esp32.in_waiting > 0:

    response = esp32.readline().decode(
        errors="ignore"
    ).strip()

    if response:

        print("ESP32:", response)

print()
print("========================================")
print("          SORTING COMPLETE")
print("========================================")

esp32.close()

print("ESP32 connection closed")
