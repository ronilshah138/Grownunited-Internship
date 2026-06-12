class Student:
    def __init__(self, student_id, name, age, course, email):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.email = email

    def to_line(self):
        return f"{self.student_id},{self.name},{self.age},{self.course},{self.email}"

    @staticmethod
    def from_line(line):
        parts = line.strip().split(',')
        if len(parts) != 5:
            return None
        return Student(int(parts[0]), parts[1], int(parts[2]), parts[3], parts[4])
