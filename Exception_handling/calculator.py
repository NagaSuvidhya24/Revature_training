from Exception_handling.ArithCalculations import  ArithCalculations
from Exception_handling.AgeNotEnoughError import AgeNotEnoughError

n1 = int(input('Enter a number: '))
n2 = int(input('Enter another number: '))
age = int(input('Enter your age: '))
cal = ArithCalculations(n1, n2)

print(f'{cal.add()}')
print(f'{cal.sub()}')
print(f'{cal.multi()}')

try:
    if n2 == 0:
        raise ZeroDivisionError('num2 is 0')
    if age < 18:
        raise AgeNotEnoughError('You are Minor')
except ZeroDivisionError as zde:
    print(f'{zde}')
except AgeNotEnoughError as anee:
    print(f'{anee}')
else:
    try:
        l1=[1,5,7,3]
        val=l1[10]
        res = cal.div()
        print(res)
    except ZeroDivisionError as zde:
        print(f'{zde} -Error!! zero in the denominator')
    except IndexError as ie:
        print(f'{ie}Index not avaliable')
    except:
        print('OopS!! Error Occured')
    else:
        #print('No Error')
        print(val)
        print(res)
    finally:
        print('Done !!')
