import numpy as np

# Sample data
students = np.array(["Amit","Neha","Rahul","Priya","Karan","Sneha","Jay","Riya"])
marks = np.array([45,78,92,67,55,88,34,95])

# Task 1
print("Task 1: Display Student Data")
for s, m in zip(students, marks):
    print(f"{s:6} : {m}")

# Task 2
print("\nTask 2: Calculate Total Marks")
print("Total Marks =", int(marks.sum()))

# Task 3
print("\nTask 3: Calculate Average Marks")
print("Average Marks =", round(marks.mean(), 2))

# Task 4
print("\nTask 4: Find Highest Scorer")
max_idx = marks.argmax()
print("Highest Marks =", int(marks[max_idx]))
print("Topper =", students[max_idx])

# Task 5
print("\nTask 5: Find Lowest Scorer")
min_idx = marks.argmin()
print("Lowest Marks =", int(marks[min_idx]))
print("Student =", students[min_idx])

# Task 6
print("\nTask 6: Pass and Fail Analysis")
pass_mark = 40
passed = students[marks >= pass_mark]
failed = students[marks < pass_mark]
print("Passed Students:")
for p in passed:
    print(p)
print("Failed Students:")
for f in failed:
    print(f)

# Task 7
print("\nTask 7: Students Above Average")
avg = marks.mean()
for s in students[marks > avg]:
    print(s)

# Task 8
print("\nTask 8: Grade Assignment")
def grade(m):
    if m >= 90:
        return 'A'
    if m >= 75:
        return 'B'
    if m >= 60:
        return 'C'
    if m >= 40:
        return 'D'
    return 'F'
for s, m in zip(students, marks):
    print(s, ":", grade(m))

# Task 9
print("\nTask 9: Top 3 Students")
order = marks.argsort()[::-1]
for i, idx in enumerate(order[:3], 1):
    print(f"{i}. {students[idx]} {marks[idx]}")

# Task 10
print("\nTask 10: Class Statistics")
print("Highest Marks :", marks.max())
print("Lowest Marks :", marks.min())
print("Average Marks :", round(avg, 2))
print("Median Marks :", float(np.median(marks)))
print("Standard Deviation :", round(np.std(marks), 2))

# Final Report
print("\nFinal Report")
print("# ==================================")
print("STUDENT PERFORMANCE REPORT")
print("Total Students :", len(students))
print("\nHighest Marks :", marks.max())
print("Topper :", students[marks.argmax()])
print("\nLowest Marks :", marks.min())
print("Lowest Performer :", students[marks.argmin()])
print("\nAverage Marks :", round(avg,2))
pass_percent = (marks >= pass_mark).sum() / len(marks) * 100
print("\nPass Percentage :", f"{pass_percent:.1f}%")
print("\nScholarship Students :")
for idx in order[:3]:
    print(students[idx])
print("\nTop 3 Students :")
for idx in order[:3]:
    print(f"{students[idx]} - {marks[idx]}")
print("# ==================================")
print("END OF REPORT")
