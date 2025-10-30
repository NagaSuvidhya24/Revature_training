'''
Date: 28-20-2025
Author:
Description: Split a string into string into equal
'''
s = input('Enter a string:')
n = int(input('Enter length of the string to split:'))

if len(s)% n !=0:
    print('Cannot divide the string into equal ')
else:
    print('String divided into equal parts:')
    for i in range(0,len(s),n):
        print(s[i:i+n])