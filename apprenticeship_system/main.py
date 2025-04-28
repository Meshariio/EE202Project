from utils.db_manager import DatabaseManager
from utils.models import Student, ApprenticeshipOpening

def main():
    db = DatabaseManager()

    student = Student(
        student_id="S001",
        name="Lina",
        mobile_number="0501234567",
        email="lina@example.com",
        gpa=4.6,
        specialization="Software Engineering",
        preferred_locations=["Riyadh", "Jeddah", "Dammam"],
        skills=["Python", "SQL", "Excel"]
    )

    existing_student = db.get_student_by_id(student.student_id)
    if existing_student:
        print(f"Student with ID {student.student_id} already exists. Skipping insertion.")
    else:
        db.add_student(student)

    opening = ApprenticeshipOpening(
        specialization="Software Engineering",
        location="Riyadh",
        stipend=2000.0,
        required_skills=["Python", "Managment", "Excel"]
    )

    db.add_opening(opening)

    print("\nStudents:")
    for s in db.get_all_students():
        print(s)

    print("\nApprenticeship Openings:")
    for o in db.get_all_openings():
        print(o)

    db.close()

if __name__ == "__main__":
    main()
