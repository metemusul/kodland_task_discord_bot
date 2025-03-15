import sqlite3
from database import get_db_connection

def test_add_task():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO tasks (description) VALUES ('Test Task')")
    conn.commit()
    c.execute("SELECT * FROM tasks WHERE description = 'Test Task'")
    task = c.fetchone()
    conn.close()
    assert task is not None

if __name__ == "__main__":
    test_add_task()
    print("Test_add_task başarıyla geçti.")