import unittest
import mysql.connector
from mysql.connector import Error

class TestSubscribersDB(unittest.TestCase):

    def setUp(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="sub_user",
            password="subpass",
            database="subscribers"
        )
        self.cursor = self.conn.cursor()

    def tearDown(self):
        self.cursor.close()
        self.conn.close()

    def test_create_subscriber(self):
        email = "test_create@example.com"
        self.cursor.execute("INSERT INTO subscribers (email) VALUES (%s)", (email,))
        self.conn.commit()

        self.cursor.execute("SELECT email FROM subscribers WHERE email = %s", (email,))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[0], email)

    def test_read_subscriber(self):
        email = "test_read@example.com"
        self.cursor.execute("INSERT INTO subscribers (email) VALUES (%s)", (email,))
        self.conn.commit()

        self.cursor.execute("SELECT id, email FROM subscribers WHERE email = %s", (email,))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[1], email)

    def test_update_subscriber(self):
        email = "test_update@example.com"
        new_email = "updated@example.com"
        self.cursor.execute("INSERT INTO subscribers (email) VALUES (%s)", (email,))
        self.conn.commit()

        self.cursor.execute("UPDATE subscribers SET email = %s WHERE email = %s", (new_email, email))
        self.conn.commit()

        self.cursor.execute("SELECT email FROM subscribers WHERE email = %s", (new_email,))
        result = self.cursor.fetchone()
        self.assertIsNotNone(result)
        self.assertEqual(result[0], new_email)

    def test_delete_subscriber(self):
        email = "test_delete@example.com"
        self.cursor.execute("INSERT INTO subscribers (email) VALUES (%s)", (email,))
        self.conn.commit()

        self.cursor.execute("DELETE FROM subscribers WHERE email = %s", (email,))
        self.conn.commit()

        self.cursor.execute("SELECT email FROM subscribers WHERE email = %s", (email,))
        result = self.cursor.fetchone()
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
