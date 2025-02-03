# Program to compute the sum of the numbers from the 1st term up to the last term input by the user

# Function to compute the sum of numbers from start to end
def compute_sum(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

# Get user input
first_term = int(input("Enter first term number: "))
last_term = int(input("Enter last term number: "))

# Compute the sum
sum_result = compute_sum(first_term, last_term)

# Display the result
print(f"The sum of the numbers from {first_term} to {last_term} is {sum_result}")

# Program to check if a given input number is a prime number

# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Get user input
num = int(input("Enter a number to check if it is prime: "))

# Check if the number is prime
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")