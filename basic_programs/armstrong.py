'''
Date : 25-10-2025
Author:
Description: using for range , for each loops
'''
numstr=input('Enter a number: ')
numlen=len(numstr)
num=int(numstr)
temp = num
#sum = 0
while num > 0:
    remainder = num % 10
    sum += remainder ** numlen
    num = num // 10
if temp == sum:
    print(f'{numstr} is a armstrong number.')
else:
    print(f'{numstr} is not a armstrong number.')

