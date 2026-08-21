def total_students(students):
    return(len(students))

def class_average(students):
    if len(students) == 0:
        return 0

    total_marks = 0
    total_subjects = 0

    for i in students:
        total_marks += sum(i.marks)
        total_subjects += len(i.marks)

    return (total_marks/total_subjects)

def highest_scorer(students):
    if len(students) == 0:
        return 0

    return max(students, key= lambda student: sum(student.marks))

def lowest_scorer(students):
    if len(students) == 0:
        return 0

    return min(students, key= lambda student: sum(student.marks))

