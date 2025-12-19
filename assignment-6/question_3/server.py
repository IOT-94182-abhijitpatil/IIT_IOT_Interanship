from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

TEMP_FILE = "temperature.txt"
LIGHT_FILE = "light.txt"

# -------- Helper function to store data --------
def store_data(filename, value):
    with open(filename, "a") as f:
        f.write(f"{datetime.now()} : {value}\n")

# -------- API to receive data from client --------
@app.route('/upload', methods=['POST'])
def upload_data():
    data = request.json

    temperature = data.get('temperature')
    light = data.get('light')

    if temperature is None or light is None:
        return jsonify({"error": "temperature and light are required"}), 400

    store_data(TEMP_FILE, temperature)
    store_data(LIGHT_FILE, light)

    return jsonify({"message": "Data stored successfully"})

# -------- API to read temperature from browser --------
@app.route('/temperature', methods=['GET'])
def get_temperature():
    try:
        with open(TEMP_FILE, "r") as f:
            data = f.read()
        return f"<pre>{data}</pre>"
    except FileNotFoundError:
        return "No temperature data available"

# -------- API to read light intensity from browser --------
@app.route('/light', methods=['GET'])
def get_light():
    try:
        with open(LIGHT_FILE, "r") as f:
            data = f.read()
        return f"<pre>{data}</pre>"
    except FileNotFoundError:
        return "No light data available"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)