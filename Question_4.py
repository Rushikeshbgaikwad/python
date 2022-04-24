z=int(input("Enter the number of row = "))
a=1
for x in range(1,z+1,+1):
    for y in range(x):
        print(a,"",end="")
        a+=1
    print()
        