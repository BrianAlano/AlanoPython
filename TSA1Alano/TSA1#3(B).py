def pattern_while():
    i = 1
    while i <= 7:
        # Print the number 'i', 'i' times
        j = 1
        while j <= i:
            print(i, end="")
            j += 1
        print()
        i += 2

pattern_while()
