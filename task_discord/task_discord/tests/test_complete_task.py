import sqlite3
from database import get_db_connection

def test_complete_task():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO tasks (description) VALUES ('Test Task')")
    conn.commit()
    task_id = c.lastrowid
    c.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    c.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    task = c.fetchone()
    conn.close()
    assert task['completed'] == 1

if __name__ == "__main__":
    test_complete_task()
    print("Test_complete_task başarıyla geçti.")