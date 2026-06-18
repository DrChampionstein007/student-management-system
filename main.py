from student import Student
from database import Database


def main():
    db = Database()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Generate 100 Dummy Students")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\n--- Add Student ---")

            student_id = input("Student ID: ")
            name = input("Name: ")
            department = input("Department: ")
            semester = int(input("Semester: "))
            email = input("Email: ")
            phone = input("Phone: ")

            student = Student(
                student_id,
                name,
                department,
                semester,
                email,
                phone
            )

            db.add_student(student)

        elif choice == "2":
            print("\n--- All Students ---")

            students = db.view_students()

            if not students:
                print("No students found.")
            else:
                for student in students:
                    print("-" * 50)
                    print(f"ID: {student['student_id']}")
                    print(f"Name: {student['name']}")
                    print(f"Department: {student['department']}")
                    print(f"Semester: {student['semester']}")
                    print(f"Email: {student['email']}")
                    print(f"Phone: {student['phone']}")

        elif choice == "3":
            print("\n--- Search Student ---")

            keyword = input("Enter keyword: ")

            results = db.search_student(keyword)

            if not results:
                print("No matching students found.")
            else:
                for student in results:
                    print("-" * 50)
                    print(f"ID: {student['student_id']}")
                    print(f"Name: {student['name']}")
                    print(f"Department: {student['department']}")
                    print(f"Semester: {student['semester']}")
                    print(f"Email: {student['email']}")
                    print(f"Phone: {student['phone']}")

        elif choice == "4":
            print("\n--- Update Student ---")

            student_id = input("Student ID: ")

            print("\nFields:")
            print("name")
            print("department")
            print("semester")
            print("email")
            print("phone")

            field = input("\nField to update: ")
            new_value = input("New value: ")

            db.update_student(student_id, field, new_value)

        elif choice == "5":
            print("\n--- Delete Student ---")

            student_id = input("Student ID: ")

            db.delete_student(student_id)

        elif choice == "6":
            db.generate_dummy_students()

        elif choice == "7":
            db.close()
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()