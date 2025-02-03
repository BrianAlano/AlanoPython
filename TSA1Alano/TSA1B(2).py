def sum_of_digits(input_string):
    total = 0

    for char in input_string:
        if char.isdigit():
            total += int(char)

    print(f"Sum of digits: {total}")


# Example usage:
input_str = input("Enter a string with digits: ")
sum_of_digits(input_str)
