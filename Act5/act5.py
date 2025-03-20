def divide(a, b):
    if b == 0:
        print("Error: Denominator must not be zero.")
        return None
    return a / b

def exponentiation(a, b):
    return a ** b

def remainder(a, b):
    if b == 0:
        print("Error: Denominator must not be zero.")
        return None
    return a % b

def summation(a, b):
    if a > b:
        print("Error: Second number must be greater than the first number.")
        return None
    return sum(range(a, b + 1))

def main():
    while True:
        print("\nMenu:")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
        
        choice = input("Enter your choice: ").upper()
        
        if choice == 'Q':
            break
        
        if choice in ['D', 'E', 'R', 'F']:
            try:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            
            if choice == 'D':
                result = divide(a, b)
            elif choice == 'E':
                result = exponentiation(a, b)
            elif choice == 'R':
                result = remainder(a, b)
            elif choice == 'F':
                result = summation(int(a), int(b))
            
            if result is not None:
                print(f"Result: {result}")
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()