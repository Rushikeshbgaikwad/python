print("Enter the number to find 'square','cube' from 0 to n")
n = int(input("Enter the value for n = "))
lst = []
for x in range(n + 1):
    lst.append(x)

print(lst)

def square(a):
    return a*a
def cube(a):
    return a**3

# k=list(map(square,lst))
# print(k)
fun=[square,cube]


# def square():
for y in (lst):
    k=list(map(lambda x: x(y),fun))
    print(k)

# squarer()

# s = (input("Enter the function name ('even','odd','square','odd','break')= "))
# while(s!="break"):
#     k=s
#     if (k=="even"):
#         even()
#     elif(k=="square"):
#         square()
#     elif(k=="cube"):
#         cube()
#     else:
#         odd()
#     k = (input("Enter the function name ('even','odd','square','odd','break')= "))
#     s=k