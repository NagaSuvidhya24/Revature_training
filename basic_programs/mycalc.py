from mypackage.interest_calculation import  simple_interest
from mypackage.mensuration import area_of_circle,area_of_recangle

prin = float(input('Principle : '))
ny = float(input('Years : '))
roi = float(input('Rate Of Intrest : '))

print(f'Simple Intrest : {simple_interest(prin = prin,ny = ny , roi = roi)[0]}' 
      f'Amount :{simple_interest(prin = prin,ny = ny , roi = roi)}[1] ')

print(f'Area of Circle : {area_of_circle(15)} \n'
      f'Area of Rectangle : {area_of_recangle(10,5) }')