import sqlite3
from sqlite3 import Error


class Database:
    def __init__(self, db_file="student.db"):
        self.db_file = db_file
        self.connection = None
        self._connect()
        self.create_table()

    def _connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            self.connection.row_factory = sqlite3.Row
        except Error as e:
            print(f"Database connection error: {e}")

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            semester INTEGER NOT NULL,
            email TEXT UNIQUE NOT NULL,
            phone TEXT NOT NULL
        );
        """

        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()

    def add_student(self, student):
        query = """
        INSERT INTO students
        (student_id, name, department, semester, email, phone)
        VALUES (?, ?, ?, ?, ?, ?)
        """

        cursor = self.connection.cursor()
        cursor.execute(query, student.to_tuple())
        self.connection.commit()

    def view_students(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM students")
        return cursor.fetchall()

    def search_student(self, keyword):
        cursor = self.connection.cursor()

        query = """
        SELECT * FROM students
        WHERE student_id LIKE ?
        OR name LIKE ?
        OR department LIKE ?
        OR email LIKE ?
        """

        pattern = f"%{keyword}%"

        cursor.execute(
            query,
            (pattern, pattern, pattern, pattern)
        )

        return cursor.fetchall()

    def update_student(self, student_id, field, new_value):
        allowed_fields = [
            "name",
            "department",
            "semester",
            "email",
            "phone"
        ]

        if field not in allowed_fields:
            print("Invalid field.")
            return

        query = f"UPDATE students SET {field}=? WHERE student_id=?"

        cursor = self.connection.cursor()
        cursor.execute(query, (new_value, student_id))
        self.connection.commit()

    def delete_student(self, student_id):
        cursor = self.connection.cursor()

        cursor.execute(
            "DELETE FROM students WHERE student_id=?",
            (student_id,)
        )

        self.connection.commit()

    def close(self):
        if self.connection:
            self.connection.close()