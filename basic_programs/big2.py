'''
Date: 25-10-2025
Author:
Description: Biggest of 2nos
'''
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))

if num1 == num2:
    print('Both numbers are equal')
elif num1 > num2:
    print(f'{num1} is greater than {num2}')
else:
    print(f'{num2} is greater than {num1}')
