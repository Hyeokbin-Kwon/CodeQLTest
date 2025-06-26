import sqlite3
import os
import subprocess

def sql_injection_example():
    # SQL Injection 취약점 예시 (시뮬레이션)
    username = "' OR '1'='1"
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT)")
    # 취약한 쿼리 문자열 직접 연결
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    print("SQL Injection result:", result)

def path_traversal_example():
    # Path Traversal 취약점 예시 (시뮬레이션)
    # 실제로 파일을 읽고 쓰기 위해 임시 파일 생성
    test_filename = "./testfile.txt"
    with open(test_filename, 'w') as f:
        f.write("This is a test file.")
    # 절대 경로 체크 없이 파일 열기
    with open(test_filename, 'r') as f:
        print("File content:", f.read())
    os.remove(test_filename)

def command_injection_example():
    # Command Injection 취약점 예시 (시뮬레이션)
    user_input = "; echo Vulnerable"
    # 사용자 입력을 직접 쉘 명령어에 삽입
    subprocess.call("ls " + user_input, shell=True)

if __name__ == "__main__":
    print("1. SQL Injection Example")
    sql_injection_example()
    print("\n2. Path Traversal Example")
    path_traversal_example()
    print("\n3. Command Injection Example")
    command_injection_example()
