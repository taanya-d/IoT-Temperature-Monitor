# IoT-Temperature-Monitor

This project simulates an IoT device that reads data from a temperature sensor and publishes it to an MQTT broker. It includes a publisher program, a subscriber program, and a server program.

## Publisher Program

The publisher program reads data from a simulated temperature sensor and publishes it to an MQTT broker every 60 seconds.

## Subscriber Program

The subscriber program reads sensor data from the MQTT broker, checks if the temperature exceeds a threshold for a certain duration, and raises an alarm. It also saves the data locally.

## Server Program

The server program exposes the sensor data on an HTTP endpoint using Flask.

## Requirements

- ESP32
- LM35
- WiFi connection

## Installation

1. Clone the repository:

```sh
git clone https://github.com/taanya-d/IoT-Temperature-Monitor.git
cd IoT-Temperature-Monitor
