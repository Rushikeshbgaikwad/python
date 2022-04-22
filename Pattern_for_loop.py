n=int(input("Enter the number for row = "))

for i in range(n):
    for j in range(i):
        print("* ",end="")
    print("")

for i in range(0,5,+1):
    for j in range (i,n,+1):
        print("* ",end="")
    print("")


# print("hello world ",end="")
# print("rushikesh babu gaikwad")