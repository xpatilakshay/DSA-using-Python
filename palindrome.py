#Taking input from user

str = input("Enter the String to check Number is palindrome or not : ") 
str = "".join(str.split()).lower()

#Checking if the string is equal to its reverse

if str==str[::-1]:
    print(f"{str} is palindrome")
else:
    print(f"{str} is not palindrome")