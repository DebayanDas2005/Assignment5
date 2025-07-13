students_marks = {'Alice': 85, 'Manashi': 90, 'Debayan': 100}
name = input("Enter the student's : ")
Name = name.capitalize()
if Name == 'Alice':
    print("{}'s mark: {} ".format(name, students_marks['Alice']))
if Name == 'Manashi':
    print("{}'s mark: {} ".format(name, students_marks['Manashi']))
if Name == 'Debayan':
    print("{}'s mark: {} ".format(name, students_marks['Debayan']))
else :
    print("Student not found.")