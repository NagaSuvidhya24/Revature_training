from oop.Employee import Employee

empid = int(input("Employee ID: "))
ename = input("Employee Name: ")
bp = float(input("Basic Pay: "))

employee = Employee(empid, ename, bp)

print(f'Emp id : {empid} \n Employee Name: {ename} \n' f'Gross Pay: {employee.calc_grosspay()} \n'
      f'Net Pay:{employee.calc_netpay()}')
