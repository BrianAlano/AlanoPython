def compute_sum(start, end):
    total = 0
    for num in range(start, end + 1):
        total += num
    return total

first_term = int(input("Enter first term number: "))
last_term = int(input("Enter last term number: "))

sum_result = compute_sum(first_term, last_term)

print(f"The sum of the numbers from {first_term} to {last_term} is {sum_result}")
