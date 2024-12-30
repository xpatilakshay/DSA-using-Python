'''
DSA Question:
1. Check if two strings have common characters
2. Convert a list of tuples to a dictionary
3. Sort a dictionary by its values in ascending order

'''

def common_character(str1,str2):
    common = []
    for char1 in str1:
        for char2 in str2:
            if char1 == char2 and char1 not in common:
                common.append(char1)
        if not common:
            print("No common found")
    print("Common Characteres are : ", common)

              
str1 = input("Enter the first string : ")
str2 = input("Enter the Second String : ")
common_character(str1,str2)




################################################### Another Way #########################################################


def common_character(str1,str2):
    str1 = set(str1)
    str2 = set(str2)
    common = str1 & str2
    return sorted(common)

str1 = input("Enter the first string : ")
str2 = input("Enter the Second String : ")
print(f"Common Characters in {str1} and {str2} are : {common_character(str1,str2)}")


