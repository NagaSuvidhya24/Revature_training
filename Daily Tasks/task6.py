'''
Date : 28-10-2025
Author:
Description: print
'''
rows = int(input("Enter rows: "))
num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
