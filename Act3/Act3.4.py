# Open the "students.txt" file in read mode
with open("students.txt", "r") as file:
    # Read the contents of the file
    contents = file.read()

# Display the student information to the user
print(contents)