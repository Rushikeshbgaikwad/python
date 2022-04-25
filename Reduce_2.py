from functools import reduce
print("Enter the 'even list' or 'odd list' = ")
str=str(input())
if (str=="even list"):
    print("Enter the number to find even number sum from 0 to n")
    n=int(input("Enter the value for n = "))
    evenlst=[]
    for x in range(n+1):
        if (x%2==0):
            evenlst.append(x)
else:
    print("Enter the number to find odd number sum from 0 to n")
    n = int(input("Enter the value for n = "))
    oddlst = []
    for x in range(n + 1):
        if (x % 2 != 0):
            oddlst.append(x)

def Evensum(a,b):
    return a+b

def Oddsum(a,b):
    return a+b

def evensum():
    k= reduce(Evensum,evenlst)
    print(k)

def oddsum():
    k= reduce(Oddsum,oddlst)
    print(k)

if (str=="even list"):
    evensum()
else:
    oddsum()