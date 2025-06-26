# 취약점 예시가 포함된 Python 코드 (SQL Injection, Path Traversal)

import sqlite3
import os

def sql_injection_example():
    # SQL Injection 취약점 예시
    username = input("Enter your username: ")
    conn = sqlite3.connect(':memory:')  # 메모리 DB 사용 (예시)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT)")
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    print("SQL Injection result:", result)

def path_traversal_example():
    # Path Traversal 취약점 예시
    filename = input("Enter file name: ")
    with open(filename, 'r') as f:
        print("File content:", f.read())

if __name__ == "__main__":
    print("1. SQL Injection Example")
    sql_injection_example()
    print("\n2. Path Traversal Example")
    path_traversal_example()
