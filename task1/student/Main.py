from StudentManager import StudentManager


def menu():
    print("\nSTUDENT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Display All Students")
    print("5. Save Data To File")
    print("6. Exit")


def add_student(manager):
    print("\nAdd Student")
    try:
        student_id = int(input("Enter Student ID: "))
    except ValueError:
        print("ID must be a number")
        return
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    email = input("Enter Email: ")
    success, message = manager.add_student(student_id, name, age, course, email)
    print(message)


def search_student(manager):
    print("\nSearch Student")
    try:
        student_id = int(input("Enter Student ID: "))
    except ValueError:
        print("ID must be a number")
        return
    student = manager.search_student(student_id)
    if student:
        print("Student Found")
        print("ID:", student.student_id)
        print("Name:", student.name)
        print("Age:", student.age)
        print("Course:", student.course)
        print("Email:", student.email)
    else:
        print("Student not found")


def delete_student(manager):
    print("\nDelete Student")
    try:
        student_id = int(input("Enter Student ID: "))
    except ValueError:
        print("ID must be a number")
        return
    success, message = manager.delete_student(student_id)
    print(message)


def display_students(manager):
    print("\nAll Students")
    students = manager.all_students()
    if not students:
        print("No students")
        return
    for s in students:
        print("ID:", s.student_id)
        print("Name:", s.name)
        print("Age:", s.age)
        print("Course:", s.course)
        print("Email:", s.email)
        print("-")


def save_data(manager):
    success, message = manager.save()
    print(message)


def main():
    manager = StudentManager("students.txt")
    while True:
        menu()
        choice = input("Enter choice: ")
        if choice == "1":
            add_student(manager)
        elif choice == "2":
            search_student(manager)
        elif choice == "3":
            delete_student(manager)
        elif choice == "4":
            display_students(manager)
        elif choice == "5":
            save_data(manager)
        elif choice == "6":
            manager.save()
            print("Goodbye")
            break
        else:
            print("Try again")


if __name__ == "__main__":
    main()
