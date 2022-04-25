from functools import reduce
print("Enter the 'even sum', 'odd sum','lst' = ")
str=str(input())
if (str=="even sum"):
    print("Enter the number to find even number sum from 0 to n")
    n=int(input("Enter the value for n = "))
    evenlst=[]
    for x in range(n+1):
        if (x%2==0):
            evenlst.append(x)
elif(str=="odd sum"):
    print("Enter the number to find odd number sum from 0 to n")
    n = int(input("Enter the value for n = "))
    oddlst = []
    for x in range(n + 1):
        if (x % 2 != 0):
            oddlst.append(x)
else:
    print("Enter the number to find 'square','cube' from 0 to n")
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
    k= reduce(Evensum,evenlst)
    print(k)

def odd():
    k= reduce(Oddsum,oddlst)
    print(k)

def square():
    for y in (lst):
        k = list(map(lambda x: x(y), sq))
        print(k,end="")

def cube():
    for z in (lst):
        k=list(map(lambda x:x(z),cu))
        print(k,end="")

def evennumber():
    k=list(filter(lambda x:x%2==0,lst))
    print(k)

def oddnumber():
    k=list(filter(lambda x:x%2!=0,lst))
    print(k)

if(str=="even sum"):
    even()
elif(str=="odd sum"):
    odd()
else:
    xz=0
    while (xz<4):
        k=input("Enter the function name 'square','cube','even number','odd number' = ")
        if(k=="square"):
            square()
        elif(k=="even number"):
            evennumber()
        elif(k=="odd number"):
            oddnumber()
        else:
            cube()
        xz=xz+1




