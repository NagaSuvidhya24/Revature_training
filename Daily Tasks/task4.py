'''
Date:28-20-2025
Author:
Description: To print pascal's triangle
'''
rows = int(input('Enter number of rows : '))

for i in range(1,rows + 1):
    print(" " * (rows - i) + "* " * i)