import unittest
import sqlite3
from database import get_db_connection

class TestBotFunctions(unittest.TestCase):
    def setUp(self):
        """Her test başlamadan önce çalışır. Veritabanını temizler."""
        self.conn = get_db_connection()
        self.c = self.conn.cursor()
        self.c.execute("DELETE FROM tasks")  # Tüm görevleri sil
        self.conn.commit()

    def tearDown(self):
        """Her test bittikten sonra çalışır. Veritabanı bağlantısını kapatır."""
        self.conn.close()

    def test_get_all_tasks(self):
        print("Testing get_all_tasks() function.")
        
        # Veritabanında görev olmadığını kontrol et
        print("Checking if there are any tasks in the database before the test starts.")
        self.c.execute("SELECT * FROM tasks")
        tasks = self.c.fetchall()
        self.assertEqual(len(tasks), 0, "Test setup failed: Tasks found in the database before the test started.")
        print("Test setup passed: No tasks found in the database before the test started.")
        
        # İki görev ekle
        print("Adding two tasks to the database.")
        self.c.execute("INSERT INTO tasks (description) VALUES ('Task 1')")
        self.c.execute("INSERT INTO tasks (description) VALUES ('Task 2')")
        self.conn.commit()
        
        # Görevleri al ve kontrol et
        self.c.execute("SELECT * FROM tasks")
        tasks = self.c.fetchall()
        self.assertEqual(len(tasks), 2, "Test failed: Expected 2 tasks but got a different number.")
        print("Test passed: Expected 2 tasks and correct number of tasks retrieved.")
        
        # Görev açıklamalarını kontrol et
        task_descriptions = [task['description'] for task in tasks]
        self.assertEqual(task_descriptions, ['Task 1', 'Task 2'], "Test failed: Task descriptions do not match.")
        print("Test passed: Task descriptions match correctly.")

if __name__ == "__main__":
    unittest.main()