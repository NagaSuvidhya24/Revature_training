'''
Date:28-7-2025
Author:
Descrition : To check whether a string is palindrome or not
'''
s1 = input('Enter a String :')
if s1 == s1[::-1]:
    print('Palindrome')
else:
    print('Not Palindrome')

#Using reversed function
s = input('Enter a String :')
rev_s = ''.join(reversed(s))

if s == rev_s:
    print('Palindrome')
else:
    print('Not Palindrome')