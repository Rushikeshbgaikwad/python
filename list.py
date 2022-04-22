marks = [97,95,91,48,52]
# print(marks)
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[:2])            #from starting to 2(it not include)
# print(marks[1:])            #from 1 to last

            # for loop in list
# for x in marks:
#     print(x)

            # use command in list
# marks.append(99)       #when you pass new element in append it is add in last of the list
# marks.insert(1,89)      #in insert you have to pass position and number to add in list
# print(93 in marks)      #you want to check number is in the list or not
# print(marks.index(97))       #you pass element then they give you position of element

# print(marks.sort())            #it will not print the sort after the process in list they print see next line
# print(marks)

marks.reverse()
print(marks)

# print(89 in marks)      #if number is in the marks then the it print true else false
# print(marks.clear())     #it is clear all list
# print(len(marks))



           #IN list there is another list
n_list =["Rushikesh",[5,9,6,3,4]]
print(n_list[1][3])