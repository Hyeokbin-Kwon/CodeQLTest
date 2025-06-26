import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# 🔒 1. 명령어 삽입 취약점 (Command Injection)
@app.route('/ping', methods=['GET'])
def ping():
    ip = request.args.get('ip', '')
    os.system("ping -c 3 " + ip)  # CodeQL: command-injection
    return "Pinged " + ip

# 🔒 2. SQL 삽입 취약점 (SQL Injection)
@app.route('/search', methods=['GET'])
def search():
    keyword = request.args.get('q', '')
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE name = '%s'" % keyword  # CodeQL: sql-injection
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return str(results)

# 🔒 3. 하드코딩된 비밀번호 (Hardcoded credential)
def check_admin_login(password):
    if password == "Admin@123":  # CodeQL: hardcoded-credentials
        return True
    return False

if __name__ == "__main__":
    app.run(debug=True)
