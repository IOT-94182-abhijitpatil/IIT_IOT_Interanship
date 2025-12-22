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
    light = data['light']
    fan = data['fan']
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

    return jsonify({"message": "Status updated successfully"})

# ---------- DISPLAY CURRENT STATUS ----------
@app.route('/status', methods=['GET'])
def get_status():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT light_status, fan_status, temperature, timestamp
        FROM home_status
        ORDER BY id DESC LIMIT 1
    """)
    status = cursor.fetchone()

    cursor.close()
    conn.close()

    if status:
        return jsonify(status)
    else:
        return jsonify({"message": "No data available"})

# ---------- Run Server ----------
if __name__ == "__main__":
    app.run(debug=True)
