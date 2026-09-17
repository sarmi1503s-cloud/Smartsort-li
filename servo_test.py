import serial
import time
PORT = "COM7"
esp32 = serial.Serial(PORT, 115200, timeout=1)
time.sleep(2)
print("SmartSort-Li Servo Test")
print("------------------------")
while True:

    command = input("Enter TEST / SAFE / HAZARD / EXIT: ").strip().upper()

    if command == "EXIT":
        break

    if command in ["TEST", "SAFE", "HAZARD"]:
        esp32.write((command + "\n").encode())
        print("Sent:", command)

    else:
        print("Invalid command")

esp32.close()
