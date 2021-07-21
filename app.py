from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)


@app.route("/")
def get_db_info():
    conn = psycopg2.connect(os.getenv('DB_URL'))
    cur = conn.cursor()
    cur.execute("SHOW ALL;")
    rows = cur.fetchall()
    return jsonify(rows)
