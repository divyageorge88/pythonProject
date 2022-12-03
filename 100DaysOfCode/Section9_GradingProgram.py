student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}

for key in student_scores:
    grade = None
    if student_scores[key] >= 91 and student_scores[key] <= 100:
        grade = "Outstanding"
    elif student_scores[key] >= 81 and student_scores[key] <= 90:
        grade = "Exceeds Expectation"
    elif student_scores[key] >=71 and student_scores[key] <= 80:
        grade = "Acceptable"
    else:
        grade = "Fail"

    student_grades[key] = grade


print(student_grades)


