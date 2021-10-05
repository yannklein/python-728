student = {
    'name': 'Lorcan',
    'age': 21,
    'hobby': 'cooking'
}
print(student)
print(len(student))
print('name' in student) # only check the keys
print('Lorcan' in student)
print('job' in student)

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

# CRUD

# C
student['job'] = 'IT engineer'
print(student)

# R
print(student['job'])
print(student.get('job', 'not found'))
print(student.get('nationality', False))

# U
student['job'] = 'Data Scientist'
print(student)

# D
del student['age']
print(student)

for key, value in student.items():
    print(f'{key} -- {value}') 