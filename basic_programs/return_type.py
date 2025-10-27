def calculate(m1,m2,m3):
    total = m1+m2+m3
    avg=total/3
    return total,avg

#sname=input("Enter your name:")
m1=int(input("Enter your first number:"))
m2=int(input("Enter your second number:"))
m3=int(input("Enter your third number:"))
total,avg=calculate(m1,m2,m3)
print(f'Total : {total}  Avg : {avg}')
# LAMBDA FUNCTION
#SQUARE OF A NUMBER
print('Square of number using lambda Exp')
sq = lambda x : x * x
print(sq(7))
# EXPESSION
print('QE using lambda Exp')
exp = lambda x,y : 2 * x+2 *y+8
print(exp(2,3))