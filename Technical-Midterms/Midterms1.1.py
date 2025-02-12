def is_palindrome(number):
    return str(number) == str(number)[::-1]

def process_line(line):
    numbers = list(map(int, line.split(',')))
    total_sum = sum(numbers)
    return total_sum, is_palindrome(total_sum)

def main():
    try:
        with open('numbers.txt', 'r') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                line = line.strip()
                if line:
                    total_sum, palindrome = process_line(line)
                    result = "Palindrome" if palindrome else "Not a palindrome"
                    print(f"Line {i + 1}: {line} (sum {total_sum}) - {result}")
    except FileNotFoundError:
        print("The file numbers.txt does not exist.")

if __name__ == "__main__":
    main()