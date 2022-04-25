from functools import reduce
print("Enter the number to create list from 0 to n = ")
n = int(input("Enter the value for n = "))
lst = []
for x in range(n):
    lst.append(x+1)

def Evensum(a,b):
    return a+b

def Oddsum(a,b):
    return a+b

def number(a):
    return a

def squareroot(a):
    return a*a

sq=[number,squareroot]

def cuberoot(a):
    return a**3

cu=[number,cuberoot]

def even():
    elst=[]
    elst=lst[1::+2]
    k= reduce(Evensum,elst)
    print(k)

def odd():
    elst = []
    elst = lst[::+2]
    k= reduce(Oddsum,elst)
    print(k)

def square():
    for y in (lst):
        k = list(map(lambda x: x(y), sq))
        print(k)

def cube():
    for z in (lst):
        k=list(map(lambda x:x(z),cu))
        print(k)

def evennumber():
    k=list(filter(lambda x:x%2==0,lst))
    print(k)

def oddnumber():
    k=list(filter(lambda x:x%2!=0,lst))
    print(k)


xz=0
while (xz<8):
    k=input("Enter the function name 'ens'=even number sum, / 'ons'=odd number sum, / 'square', / 'cube', / 'even number', / 'odd number', / 'break' = ")
    if(k=="break"):
        break
    elif (k == "ens"):
        even()
    elif (k == "ons"):
        odd()
    elif(k=="square"):
        square()
    elif(k=="even number"):
        evennumber()
    elif(k=="odd number"):
        oddnumber()
    else:
        cube()
    xz=xz+1




