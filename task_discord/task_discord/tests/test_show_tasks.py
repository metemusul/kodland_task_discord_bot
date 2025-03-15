import sqlite3
from database import get_db_connection

def test_show_tasks():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO tasks (description) VALUES ('Test Task 1')")
    c.execute("INSERT INTO tasks (description) VALUES ('Test Task 2')")
    conn.commit()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    assert len(tasks) == 2

if __name__ == "__main__":
    test_show_tasks()
    print("Test_show_tasks başarıyla geçti.")