'''
Date:28-10-2025
Author:
Description:converting camel case into snake case
'''
s = input('Enter Camel case String:')
new = " "
for ch in s:
    if ch.isupper():
        new +="_" + ch.lower()
    else:
        new +=ch
print('Snake Case:',new.lstrip("_"))