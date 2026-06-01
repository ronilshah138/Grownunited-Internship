from Student import Student

class StudentManager:
    def __init__(self, filename="students.txt"):
        self.filename = filename
        self.students = []
        self.load()

    def add_student(self, student_id, name, age, course, email):
        if any(s.student_id == student_id for s in self.students):
            return False, "Student ID already exists"
        if not name.strip():
            return False, "Name cannot be empty"
        try:
            age = int(age)
            if age <= 0:
                return False, "Age must be greater than 0"
        except ValueError:
            return False, "Age must be a number"
        if "@" not in email:
            return False, "Email must contain @"

        self.students.append(Student(student_id, name, age, course, email))
        return True, "Student added successfully"

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def delete_student(self, student_id):
        for i, student in enumerate(self.students):
            if student.student_id == student_id:
                self.students.pop(i)
                return True, "Student deleted successfully"
        return False, "Student not found"

    def save(self):
        with open(self.filename, "w") as file:
            for student in self.students:
                file.write(student.to_line() + "\n")
        return True, "Data saved"

    def load(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    student = Student.from_line(line)
                    if student:
                        self.students.append(student)
        except FileNotFoundError:
            pass

    def all_students(self):
        return self.students
