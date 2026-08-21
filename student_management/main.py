from student_addition import Student
from operations import search_student, update_student, delete_student
from stats import total_students, class_average, highest_scorer, lowest_scorer

students = []

with open("student_record.txt","r") as file:

    for line in file:

        data = line.strip().split(",")
        name = data[0]
        rollnumber = data[1]
        age = data[2]

        marks = []
        for j in data[3:]:
            marks.append(int(j))

        student = Student(rollnumber,name,age,marks)
        students.append(student)

while True:
    
    print("*" *40)
    print(f"{'STUDENT MANAGEMENT SYSTEM':^40}")
    print("*" *40)

    print("1. Search Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Print All Students")
    print("5. Class Statistics")
    print("6. Exit")

    choice = input("Enter your choice: ")
    
    if choice == "1":
        rollnumber = input("Enter roll number to search: ")
        
        student = search_student(students, rollnumber)
        
        if student:
            print("\nStudent Found!")
            print(f"Name       : {student.name}")
            print(f"Roll Number: {student.rollnumber}")
            print(f"Age        : {student.age}")
            print(f"Marks      : {student.marks}")
        
        else:
            print("Student not found.")

    elif choice == "2":

        rollnumber = input("Enter the rollnumber to be updated: ")
        result = update_student(students,rollnumber)
        
        if result:
            print("Student updated successfully.")
        else:
            print("Student not found.")


    elif choice == "3":

        rollnumber = input("Enter roll number to delete: ")

        result = delete_student(students, rollnumber)

        if result:
            print("Student deleted successfully.")

        else:
            print("Student not found.")

    elif choice == "4":
        for s in students:
            print("\n")
            print("*" *40)
            print(f"{'STUDENT RECORD':^40}")
            print("*" *40)
            print(f"{'NAME':<12}:  |{s.name:>10}|")
            print(f"{'ROLLNUMBER':<12}:  |{s.rollnumber:>10}|")
            print(f"{'AGE':<12}:  |{s.age:>10}|")
            print(f"{'MARKS':<12}:  |{str(s.marks):>10}|")
            print("*" *40)

    elif choice == "5":
        total = total_students(students)
        average = class_average(students)
        highest = highest_scorer(students)
        lowest = lowest_scorer(students)

        print("\n")
        print("*" * 40)
        print(f"{'CLASS STATISTICS':^40}")
        print("*" * 40)

        print(f"Total Students : {total}")
        print(f"Class Average  : {average:.2f}")

        if highest:
            print(f"Highest Scorer : {highest.name}")
            print(f"Highest Marks  : {sum(highest.marks)}")

        if lowest:
            print(f"Lowest Scorer  : {lowest.name}")
            print(f"Lowest Marks   : {sum(lowest.marks)}")

        print("*" * 40)

    elif choice == "6":

        print("Exiting program...")
        break

    else:
        print("Invalid choice.")