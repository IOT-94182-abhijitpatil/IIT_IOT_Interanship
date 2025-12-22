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
        database="iot_data"
    )

# ---------- CREATE (Insert) ----------
@app.route('/insert', methods=['POST'])
def insert_record():
    data = request.json
    temperature = data['temperature']
    humidity = data['humidity']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO sensor_readings (temperature, humidity, timestamp)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (temperature, humidity, datetime.now()))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Record inserted successfully"})

# ---------- READ (All Records) ----------
@app.route('/read', methods=['GET'])
def read_all():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM sensor_readings")
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(records)

# ---------- UPDATE ----------
@app.route('/update/<int:id>', methods=['PUT'])
def update_record(id):
    data = request.json
    temperature = data['temperature']
    humidity = data['humidity']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    UPDATE sensor_readings
    SET temperature=%s, humidity=%s
    WHERE id=%s
    """
    cursor.execute(query, (temperature, humidity, id))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Record updated successfully"})

# ---------- DELETE ----------
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_record(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM sensor_readings WHERE id=%s", (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Record deleted successfully"})

# ---------- READ BELOW THRESHOLD ----------
@app.route('/below/<float:threshold>', methods=['GET'])
def below_threshold(threshold):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM sensor_readings WHERE temperature < %s"
    cursor.execute(query, (threshold,))
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(records)

# ---------- Run Server ----------
if __name__ == "__main__":
    app.run(debug=True)
