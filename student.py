class Student:
    def __init__(self, student_id, name, department, semester, email, phone):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.semester = semester
        self.email = email
        self.phone = phone

    def to_tuple(self):
        return (
            self.student_id,
            self.name,
            self.department,
            self.semester,
            self.email,
            self.phone
        )

    def __str__(self):
        return (
            f"ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Department: {self.department}\n"
            f"Semester: {self.semester}\n"
            f"Email: {self.email}\n"
            f"Phone: {self.phone}"
        )