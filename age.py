# assigning the user input to variable age
# CAREFUL: input() returns a str
age = int(input('What\'s your age? '))

# print the age in one year
# print(age + 1)

# Your age is XX next year
# concatenation
# print("Your age is " + str(age + 1) + " in one year")

# interpolation
print(f'Your age is { age + 1 } next year')