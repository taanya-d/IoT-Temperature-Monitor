from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Global list to store historical sensor data
sensor_data_list = []

@app.route('/temperature', methods=['POST'])
def receive_temperature():
    data = request.get_json()
    if 'temperature' in data:
        temperature = data['temperature']
        timestamp = datetime.now().isoformat()
        sensor_data = {
            'temperature': temperature,
            'timestamp': timestamp
        }
        sensor_data_list.append(sensor_data)
        return jsonify(sensor_data), 200
    else:
        return jsonify({"error": "Invalid data"}), 400

@app.route('/temperature', methods=['GET'])
def get_temperature():
    if sensor_data_list:
        return jsonify(sensor_data_list[-1])  # Return the latest sensor data
    else:
        return jsonify({"error": "No data available"}), 404

@app.route('/temperature/all', methods=['GET'])
def get_all_temperature():
    if sensor_data_list:
        return jsonify(sensor_data_list)  # Return all sensor data
    else:
        return jsonify({"error": "No data available"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
