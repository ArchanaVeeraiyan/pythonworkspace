def students_report(student_name, marks):
    if marks >= 70:
        grade = "distinction"

    elif marks >= 60:
        grade = "second class"

    elif marks >= 50:
        grade = "Third class"

    else:
        grade = "fail"

    return f"{student_name}: {marks} - {grade}"

print(students_report("Archana1", 85))
print(students_report("Archana2", 55))
print(students_report("Archana3", 45))         