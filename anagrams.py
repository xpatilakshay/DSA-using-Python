def are_anagrams(str1,str2):
    str1 = sorted(str1)
    str2 = sorted(str2)
    if str1 == str2:
        return True
    else:
        return False
    
str1 = input("Enter the first string : ")
str2 = input("Enter the Second String : ")

if are_anagrams(str1,str2):
    print(f"{str1} and {str2} are anagrams")
else:
    print(f"{str1} and {str2} are not anagrams")

