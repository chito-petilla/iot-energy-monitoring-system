from flask import Flask, request, jsonify
import sqlite3
import time

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect("../database/iot.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS EnergyReadings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT,
            voltage REAL,
            current REAL,
            power REAL,
            timestamp REAL
        )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route("/api/data", methods=["POST"])
def receive_data():
    data = request.json

    voltage = data["voltage"]
    current = data["current"]
    power = voltage * current

    conn = sqlite3.connect("../database/iot.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO EnergyReadings (device_id, voltage, current, power, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (
        data["device_id"],
        voltage,
        current,
        power,
        time.time()
    ))

    conn.commit()
    conn.close()

    return jsonify({"status": "stored", "power": power})

@app.route("/api/latest")
def latest():
    conn = sqlite3.connect("../database/iot.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM EnergyReadings ORDER BY id DESC LIMIT 10")
    rows = cursor.fetchall()

    conn.close()

    return jsonify(rows)

if __name__ == "__main__":
    app.run(debug=True)
