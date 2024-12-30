'''
3. Sort a dictionary by its values in ascending order

'''

student = {"firt":"dinesh","second":"rajesh","third":"Akshay"}
sorted_dict_by_val = dict(sorted(student.items(),key = lambda item : item[1]))
print(sorted_dict_by_val)