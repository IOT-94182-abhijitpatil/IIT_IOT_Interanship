from flask import Flask, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# ---------- Database Connection ----------
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="smart_home"
    )

# ---------- UPDATE SENSOR DATA ----------
@app.route('/update', methods=['POST'])
def update_status():
    data = request.json

    light = data['light_status']   # ON / OFF
    fan = data['fan_status']       # ON / OFF
    temperature = data['temperature']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO home_status
    (light_status, fan_status, temperature, timestamp)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (light, fan, temperature, datetime.now()))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Smart home status updated successfully"})

# ---------- DISPLAY CURRENT STATUS ----------
@app.route('/status', methods=['GET'])
def get_status():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT light_status, fan_status, temperature
    FROM home_status
    ORDER BY timestamp DESC
    LIMIT 1
    """
    cursor.execute(query)
    status = cursor.fetchone()

    cursor.close()
    conn.close()

    if status:
        return jsonify({
            "Light": status["light_status"],
            "Fan": status["fan_status"],
            "Temperature": status["temperature"]
        })
    else:
        return jsonify({"message": "No data available"})

# ---------- Run Server ----------
if __name__ == "__main__":
    app.run(debug=True)
