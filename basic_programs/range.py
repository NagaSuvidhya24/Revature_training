terms = int(input('Enter number of terms: '))
sum =0
for num in range(1,terms+1):
    sum += num * num

print(sum)

# using for each loop
sqnum=[]
numbers = [10,20,30,40,50]
for num in numbers:
    print(num)
    sqnum.append(num)
# to convert list into tuple
tuple1=tuple(sqnum)
print(tuple1)
# to convert list into set
set1=set(sqnum)
print(set1)
# to convert list into dictonary
dnum = dict()
for num in numbers:
    dnum[num]=num * num
print(dnum)

