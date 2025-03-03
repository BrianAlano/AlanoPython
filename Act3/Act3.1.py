# 3.1. Activity for Performing String Manipulations

# Concatenate first name and last name into a full name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
last_name = "Alano"
full_name = first_name + " " + last_name

# Slice the full name to extract the first three characters of the first name
sliced_first_name = first_name[:3]

# Use string formatting to create a greeting message that includes the sliced first name
greeting_message = f"Hello, {sliced_first_name}!"

# Print the results
print("Full Name:", full_name)
age = 25  # Example age
print("Age:", age)
print("Sliced First Name:", sliced_first_name)