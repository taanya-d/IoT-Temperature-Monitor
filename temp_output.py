import time
import requests
import json
from random import uniform

# WiFi credentials and server URL
ssid = "SNBTech"  # use your ssid
password = "myanimal@042022"  # use your password
server_url = "http://192.168.89.177:5000/temperature"  # Replace with your Flask server's IP address

def read_temperature():
    # Simulate reading the analog value from the LM35 sensor
    analog_value = uniform(0, 4095)  # Simulated analog reading

    # Convert the analog value to a temperature in Celsius
    voltage = analog_value * (3.3 / 4095.0)  # ADC resolution is 12 bits (4095)
    temperature_c = voltage * 100.0  # LM35 output is 10mV per degree Celsius
    return temperature_c

def send_temperature(temperature):
    headers = {'Content-Type': 'application/json'}
    data = {'temperature': round(temperature, 2)}
    try:
        response = requests.post(server_url, headers=headers, data=json.dumps(data))
        print(response.status_code)
        print(response.text)
    except requests.RequestException as e:
        print(f"Error sending POST request: {e}")

def main():
    print("Connecting to WiFi...")
    time.sleep(2)  # Simulate WiFi connection delay
    print("Connected!")

    while True:
        temperature = read_temperature()
        print(f"Temperature: {temperature:.2f} C")
        
        send_temperature(temperature)
        time.sleep(60)  # Send data every 60 seconds

if __name__ == "__main__":
    main()
