'''
Date : 27-10-2025
Author:
Description: Types of ways to pass values to arguments
'''

#keyarbitary_arguments
def add(**nums):
    print("Received nums:",(nums))
    res = nums['fn'] + nums['sn'] + nums['tn']
    return res

#input and output
n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
n3 = int(input('Enter third number: '))

print("Sum:",add(fn=n1,sn=n2,tn = n3))

#Arbitary_parameters
def add(*,nums):
    res = 0
    for num in nums:
        res =res + num
    return res

n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
n3 = int(input('Enter third number: '))
n4 = int(input('Enter fourth number: '))
print(n1,n2,n3,n4)

#optional_parameter
def add(n1,n2,n3,n4):
    res = n1 + n2 + n3 + n4
    return res
n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
n3 = int(input('Enter third number: '))
n4 = int(input('Enter fourth number: '))

print(n1,n2,n3,n4)

