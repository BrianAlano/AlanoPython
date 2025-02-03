def count_characters(input_string):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    spaces = 0
    vowel_count = 0
    consonant_count = 0
    other_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
        elif char == " ":
            spaces += 1
        else:
            other_count += 1

    print(f"Vowels: {vowel_count}")
    print(f"Consonants: {consonant_count}")
    print(f"Spaces: {spaces}")
    print(f"Other characters: {other_count}")

input_str = input("Enter a string: ")
count_characters(input_str)
