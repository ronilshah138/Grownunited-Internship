def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def is_passed(marks):
    return marks >= 50


def calculate_average(marks_list):
    if len(marks_list) == 0:
        return 0
    return sum(marks_list) / len(marks_list)



students = {}


num_students = int(input("Enter number of students: "))

for i in range(num_students):
    name = input(f"\nEnter Student {i + 1} Name: ")
    marks = float(input(f"Enter {name}'s Marks: "))
    grade = calculate_grade(marks)
    passed = is_passed(marks)
    
    students[name] = {
        "marks": marks,
        "grade": grade,
        "status": "Passed" if passed else "Failed"
    }


print("\n" + "="*45)
print("         STUDENT GRADE REPORT")
print("="*45)

for name, info in students.items():
    print(f"\nName: {name}")
    print(f"Marks: {info['marks']}")
    print(f"Grade: {info['grade']}")
    print(f"Status: {info['status']}")


all_marks = [info["marks"] for info in students.values()]
average = calculate_average(all_marks)
print(f"\nClass Average: {average:.2f}")
print("="*45)
