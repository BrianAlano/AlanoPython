from collections import Counter

# Input the user's first name and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenate the input names into a full name
full_name = first_name + " " + last_name
# Display the full name
print("Full name: ", full_name)
# Display the full name in both upper and lower case
print("Full name in upper case: ", full_name.upper())
print("Full name in lower case: ", full_name.lower())

# Count and display the length of the full name
print("Length of the full name: ", len(full_name))
