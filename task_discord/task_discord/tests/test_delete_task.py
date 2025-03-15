import sqlite3
from database import get_db_connection

def test_delete_task():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO tasks (description) VALUES ('Test Task')")
    conn.commit()
    task_id = c.lastrowid
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    c.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = c.fetchone()
    conn.close()
    assert task is None

if __name__ == "__main__":
    test_delete_task()
    print("Test_delete_task başarıyla geçti.")