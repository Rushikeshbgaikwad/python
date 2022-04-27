from functools import reduce
print("Enter the number to create list from 0 to n = ")
n = int(input("Enter the value for n = "))
lst = []
for x in range(n):
    lst.append(x+1)

def Evensum(a,b):  #even using reduce
    return a+b

def Oddsum(a,b):   #odd using reduce
    return a+b

def prime(lst):
    prime = []
    for y in lst:
        count = 0
        for z in lst:
            if y % z == 0:
                count = count + 1
        if count == 2:
            prime.append(y)
    return (prime)

def number(a):      #sq,cu, using map
    return a

def squareroot(a):         #sq  using map
    return a*a

sq=[number,squareroot]

def cuberoot(a):           #cu,   using map
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

def evennumber():           #using filter
    k=list(filter(lambda x:x%2==0,lst))
    print(k)

def oddnumber():            ##using filter
    k=list(filter(lambda x:x%2!=0,lst))
    print(k)

def prime_no():
    k=prime(lst)
    print(k)

def prime_sum():
    k=prime(lst)
    n=reduce(lambda x,y:x+y,k)
    print(n)

xz=0
while (xz<10):
    k=input("Enter the function name 'ens'=even number sum, / 'ons'=odd number sum, / 'square', / 'cube', / 'even number', / 'odd number', / 'prime no' / 'prime sum', / 'break', / = ")
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
    elif(k=="prime no"):
        prime_no()
    elif(k=="prime sum"):
        prime_sum()
    else:
        cube()
    xz=xz+1




