def get_user_input():
    import sqlite3
    # 사용자 입력을 받음
    username = input("Enter your username: ")
    # 데이터베이스 연결
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # SQL Injection 가능성이 있는 쿼리
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

if __name__ == "__main__":
    print(get_user_input())