'''
Date : 28-10-2025
Author:
Description : Remove Duplicates from string
'''
s = input('Enter a string: ')
result = ""
for ch in s:
    if ch not in result:
        result += ch
print("After removing duplicates:", result)