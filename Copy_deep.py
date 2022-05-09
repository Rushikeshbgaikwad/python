import copy

# list1=[1,2,3,4,5]
# list2=copy.deepcopy(list1)
# list2[1]=150
# print(list1)
# print(id(list1))
# print(list2)
# print(id(list2))


list1=[[1,2,3],[4,5,6],[7,8,9]]
list2=copy.deepcopy(list1)
list2[2][1]=1560
print(list1)
print(id(list1))
print(list2)
print(id(list2))