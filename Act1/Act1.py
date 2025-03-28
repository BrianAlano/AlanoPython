def find_highest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        highest = num1
    elif num2 >= num1 and num2 >= num3:
        highest = num2
    else:
        highest = num3
    return highest

def display_descending(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        if num2 >= num3:
            print(num1, num2, num3)
        else:
            print(num1, num3, num2)
    elif num2 >= num1 and num2 >= num3:
        if num1 >= num3:
            print(num2, num1, num3)
        else:
            print(num2, num3, num1)
    else:
        if num1 >= num2:
            print(num3, num1, num2)
        else:
            print(num3, num2, num1)

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

highest = find_highest(num1, num2, num3)
print(f"The highest number is: {highest}")

print("The numbers in descending order are: ")
display_descending(num1, num2, num3)