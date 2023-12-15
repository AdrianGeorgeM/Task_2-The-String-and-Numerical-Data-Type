# String to manipulate
# str_manip = "This is a bunch of words"
str_manip = input("Enter a string to manipulate: ")

# Task 1: Calculate and display the length of str_manip
length_of_str = len(str_manip)

# Task 2: Replace the last letter in str_manip with '@'
last_letter = str_manip[-1]
replace_letter = str_manip.replace(last_letter,"@")


# Task 3: Print the last 3 characters in str_manip backwards
last_3_chars = str_manip[-1:-4:-1] #[start:end:step]  the last three characters
# Start (-1): Start at (the last character).
# End (-4): Go up to (but not including) "-4" (the fourth character from the end).
# Step (-1): Move backward by one character at a time.
# print(last_3_chars )

# Task 4: Create a five-letter word from the first three and last two characters in str_manip
five_letter_word = str_manip[:3] + str_manip[-2:]
print(f"Length of the string: {length_of_str}")
print(f"Modified string: {replace_letter}")
print(f"Last 3 characters backwards: {last_3_chars}")
print(f"Five-letter word: {five_letter_word}")


