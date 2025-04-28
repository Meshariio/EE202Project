import sqlite3
from utils.models import Student, ApprenticeshipOpening

class DatabaseManager:
    def __init__(self, db_name="data/apprenticeship_matching.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            mobile_number TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            gpa REAL CHECK(gpa >= 0 AND gpa <= 5),
            specialization TEXT NOT NULL,
            skills TEXT,
            preferred_location_1 TEXT,
            preferred_location_2 TEXT,
            preferred_location_3 TEXT
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS openings (
            opening_id INTEGER PRIMARY KEY AUTOINCREMENT,
            specialization TEXT NOT NULL,
            location TEXT NOT NULL,
            stipend REAL CHECK(stipend > 0),
            required_skills TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def add_student(self, student: Student):
        data = student.to_dict()
        try:
            self.cursor.execute("""
            INSERT INTO students (
                student_id, name, mobile_number, email, gpa,
                specialization, skills,
                preferred_location_1, preferred_location_2, preferred_location_3
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                data["student_id"], data["name"], data["mobile_number"], data["email"],
                data["gpa"], data["specialization"], data["skills"],
                data["preferred_location_1"], data["preferred_location_2"], data["preferred_location_3"]
            ))
            self.conn.commit()
            print("Student added successfully.")
        except sqlite3.IntegrityError as e:
            print("Error adding student:", e)

    def get_all_students(self):
        self.cursor.execute("SELECT * FROM students")
        return self.cursor.fetchall()

    def get_student_by_id(self, student_id: str):
        self.cursor.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
        return self.cursor.fetchone()

    def update_student(self, student: Student):
        data = student.to_dict()
        self.cursor.execute("""
        UPDATE students
        SET name = ?, mobile_number = ?, email = ?, gpa = ?, specialization = ?, skills = ?,
            preferred_location_1 = ?, preferred_location_2 = ?, preferred_location_3 = ?
        WHERE student_id = ?
        """, (
            data["name"], data["mobile_number"], data["email"], data["gpa"],
            data["specialization"], data["skills"],
            data["preferred_location_1"], data["preferred_location_2"], data["preferred_location_3"],
            data["student_id"]
        ))
        self.conn.commit()
        print(f"Student with ID {student.student_id} updated.")

    def delete_student(self, student_id: str):
        self.cursor.execute("DELETE FROM students WHERE student_id = ?", (student_id,))
        self.conn.commit()
        print(f"Student with ID {student_id} deleted.")

    def add_opening(self, opening: ApprenticeshipOpening):
        data = opening.to_dict()
        try:
            self.cursor.execute("""
            INSERT INTO openings (specialization, location, stipend, required_skills)
            VALUES (?, ?, ?, ?)
            """, (
                data["specialization"], data["location"], data["stipend"], data["required_skills"]
            ))
            self.conn.commit()
            print("Apprenticeship opening added successfully.")
        except sqlite3.IntegrityError as e:
            print("Error adding opening:", e)

    def get_all_openings(self):
        self.cursor.execute("SELECT * FROM openings")
        return self.cursor.fetchall()

    def delete_opening(self, opening_id: int):
        self.cursor.execute("DELETE FROM openings WHERE opening_id = ?", (opening_id,))
        self.conn.commit()
        print(f"Apprenticeship opening with ID {opening_id} deleted.")

    def update_opening(self, opening_id: int, opening: ApprenticeshipOpening):
        data = opening.to_dict()
        self.cursor.execute("""
        UPDATE openings
        SET specialization = ?, location = ?, stipend = ?, required_skills = ?
        WHERE opening_id = ?
        """, (
            data["specialization"], data["location"], data["stipend"], data["required_skills"],
            opening_id
        ))
        self.conn.commit()
        print(f"Apprenticeship opening with ID {opening_id} updated.")

    def close(self):
        self.conn.close()
