n=int(input("Enter the number to check from 0 to ="))
lst =[]
for x in range(n):
    lst.append(x+1)

# for x in (lst):
#     print(x)

def number(a):
    return a

def square(a):
    return a*a

def cube(a):
    return a**3

fun=[number,square,cube]
for y in (lst):
    k=list(map(lambda x: x(y),fun))
    print(k)

#
# k=list(filter(lambda x:x%2==0,lst))
# print(k)
#
# q=list(filter(lambda x:x%2!=0,lst))
# print(q)
#
# w=list(map(lambda x:x%2==0,lst))
# print(w)
#
# z=list(map(lambda x:x%2!=0,lst))
# print(z)