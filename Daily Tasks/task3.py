'''
Date : 28 -10-2025
Author:
Description : Count the number vowels in a string
'''
s = input('Enter a String: ')
str = s.lower()
count = 0
for ch in s :
    #if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    if ch in "aeiou":
        count = count + 1
print('Vowels count', count)

