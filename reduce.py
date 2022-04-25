from functools import reduce

print("Enter the number to find even number sum from 0 to n")
n=int(input("Enter the value for n = "))
evenlst=[]
for x in range(n+1):
    if (x%2==0):
        evenlst.append(x)

# print(evenlst)

sum=reduce((lambda q,y: q+y ),evenlst)
print(sum)


print("Enter the number to find odd number odd from 0 to n")
n=int(input("Enter the value for n = "))
oddlst=[]
for x in range(n+1):
    if (x%2!=0):
        oddlst.append(x)

# print(oddlst)

sum=reduce((lambda q,y: q+y ),oddlst)
print(sum)

