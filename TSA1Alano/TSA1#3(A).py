def pattern_for():
    for i in range(1, 6):
        # Print spaces first
        for j in range(5 - i):
            print(" ", end="")
        # Print numbers
        for k in range(1, i + 1):
            print(k, end="")
        print()

# Call the function to display the pattern
pattern_for()
