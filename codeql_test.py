import os
import sqlite3

# 하드코딩된 비밀번호 (Hardcoded credentials)
DB_PASSWORD = "supersecret123"  # CodeQL: hardcoded-credentials

def execute_command(user_input):
    # OS 명령어 삽입 취약점 (Command Injection)
    os.system("ping " + user_input)  # CodeQL: command-injection

def login(username, password):
    if password == DB_PASSWORD:
        print("Access granted")
    else:
        print("Access denied")

def search_user(user_input):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    # SQL Injection
    query = f"SELECT * FROM users WHERE name = '{user_input}'"  # CodeQL: sql-injection
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    conn.close()

if __name__ == "__main__":
    name = input("Enter your name: ")
    execute_command(name)

    username = input("Username: ")
    password = input("Password: ")
    login(username, password)

    keyword = input("Search keyword: ")
    search_user(keyword)