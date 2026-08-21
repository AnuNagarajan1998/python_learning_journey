def search_student(students, rollnumber):

    for student in students:
        if student.rollnumber == rollnumber:
            return student
    return None

def update_student(students, rollnumber):

    student = search_student(students,rollnumber)

    if student is None:
        return False

    print("\n Student found!")

    student.name = input("Enter the name: ")
    student.age = input("Enter the age: ")

    student.marks = []

    for i in range(5):
        mark = int(input(f"Enter the marks {i+1}: "))
        student.marks.append(mark)

    return True

def delete_student(students,rollnumber):

    student =search_student(students, rollnumber)

    if student is None:
        return False

    students.remove(student)

    return True