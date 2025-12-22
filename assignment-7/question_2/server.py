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
        database="smart_agri"
    )

# ---------- CREATE (Insert) ----------
@app.route('/insert', methods=['POST'])
def insert_record():
    data = request.json
    sensor_id = data['sensor_id']
    moisture = data['moisture_level']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO soil_moisture_readings
    (sensor_id, moisture_level, reading_time)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (sensor_id, moisture, datetime.now()))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Record inserted successfully"})

# ---------- READ (All Records) ----------
@app.route('/read', methods=['GET'])
def read_all():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM soil_moisture_readings")
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(records)

# ---------- UPDATE ----------
@app.route('/update/<int:sensor_id>', methods=['PUT'])
def update_record(sensor_id):
    data = request.json
    moisture = data['moisture_level']

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    UPDATE soil_moisture_readings
    SET moisture_level = %s, reading_time = %s
    WHERE sensor_id = %s
    """
    cursor.execute(query, (moisture, datetime.now(), sensor_id))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Record updated successfully"})

# ---------- DELETE ----------
@app.route('/delete/<int:sensor_id>', methods=['DELETE'])
def delete_record(sensor_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM soil_moisture_readings WHERE sensor_id = %s",
        (sensor_id,)
    )
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Record deleted successfully"})

# ---------- READ BELOW THRESHOLD ----------
@app.route('/below/<float:threshold>', methods=['GET'])
def below_threshold(threshold):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT * FROM soil_moisture_readings
    WHERE moisture_level < %s
    """
    cursor.execute(query, (threshold,))
    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(records)

# ---------- Run Server ----------
if __name__ == "__main__":
    app.run(debug=True)
