'''
Date : 28-10-2025
Author :
Description: print all the prime numbers in an intervel
'''

#Reading input
start = int(input('Enter start number: '))
end = int(input('Enter end number: '))
#loop to print all prime numbers
for num in range (start,end +1):
    if num > 1 :
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=' ')
