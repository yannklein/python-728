#               0           1         2        3
students = ['Elizabeth', 'Risako', 'Larry', 'Nadia']
print(students)
print(len(students))
print('Larry' in students)
print('Alexis' in students)
print(students[1]) # returns a str
print(students[:2]) # from start to 2 excluded, returns a list (subset)
print(students[1:2]) # from 1 to 2 excluded, returns a list (subset)
print(students[-2]) # 2nd to last element of the list, returns a str

# CRUD

# Create
students.append('Alexis')
students.insert(2, 'Jack')
print(students)

# Read
print(students[3])

# Update
students[3] = 'Super Larry'
print(students)

# Delete
del students[3]
print(students)

# for student in students:
#     print(f'{student} is great!')

# print(list(enumerate(students)))
# for index, student in enumerate(students):
#     print(f'{index + 1} - {student} is great!')

# [ print(f'{student} is great!') for student in students ]

student_uppercase = [ student.upper() for student in students ]
print(student_uppercase)