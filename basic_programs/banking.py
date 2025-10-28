""" Banking Interest Calculation"""

from mypackage.interest_calculation import simple_interest,compound_interest

prin = float(input('Principle : '))
ny = float(input('Years : '))
roi = float(input('Rate Of Intrest : '))

si, amt = simple_interest(prin = prin,ny = ny , roi = roi)
print(f'Simple Intrest :{si} Amount : {amt}')

amt = compound_interest(prin = prin,t = ny , roi = roi)
print(f'Compound Interest :{amt}')
