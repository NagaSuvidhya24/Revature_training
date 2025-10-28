#from student details import Stud
from oop.studexcurr import StudExCurr

ccode = input('ccode: ')
cname = input('cname: ')
rollno = int(input("Roll no: "))
sname = input("Name: ")
m1 = int(input("Mark 1: "))
m2 = int(input("Mark 2: "))
m3 = int(input("Mark 3: "))
exm1=int(input("Ex mark 1: "))
exm2=int(input("Ex mark 2: "))

stud = StudExCurr(ccode,cname,rollno,sname,m1,m2,m3,exm1,exm2)

print(f'{stud.display()[0]} \t {stud.display()[1]}' )
print(f'{stud.get_rollno()}\n {stud.get_sname()}\n '
      f'{stud.calc_tot()}\n {stud.calc_avg()}')
print(f'{stud.calc_extot()}')
