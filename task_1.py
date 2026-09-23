
# Creating a dictionary of student's and marks

students = {"John":85, "Alice":94, "Dan":79, "Rahul":91}

# we can add a .capitalize() to make it case friendly if we want
# i am writing both just in case if we want to use another
while True:
    student_name = input("Enter the student's name: ")
    # student_name = input("Enter the student's name: ").capitalize()

    try:
        marks = students[student_name]
        print(f"{student_name}'s marks: {marks}")
        break

    except KeyError:
        print("Student not found")
        break


