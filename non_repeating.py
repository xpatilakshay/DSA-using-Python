def first_non_repeating_character(str):
    for char in str:
        if str.count(char) == 1:
            return char

str = input("Enter the string : ")
if first_non_repeating_character(str):
    print(f"first non-repeating character is {first_non_repeating_character(str)}")
else:
    print("There is no non-repeating character in a string")