# marks = (81,83,85,87,89,91,93,95,97,99,82,81,83,81)
#[] = list
#() = tuple
#{} = set
# print("position of 91 = " +str(marks.index(91)))          #index is use to find position of item
# print("count of 81 = " +str(marks.count(81)))             #count is used for how many time that element come in tuple and list
# print(type(marks))

# tuplex=(4,6,2,8,3,1)
# print(tuplex)
#
# tuplex=tuplex+(9,)
# print(tuplex)
#
# tuplex=tuplex[:5]+(15,20,25)+tuplex[:2]
# print(tuplex)
#
# listx=list(tuplex)
# listx.append(30)
# tuplex=tuple(listx)
# print(tuplex)

# name=tuple("Rushikesh")
# print(name)
# print(len(name))

name1=tuple("Hello world")
slice = name1[-2:-9:-3]
print(slice)