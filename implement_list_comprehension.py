l1=['x','y','z']
lst1=[i*j for j in l1 for i in range(1,5)]
print(lst1)

l2=['x','y','z']
lst2=[i*j for j in range(1,5) for i in l2]
print(lst2)

lst3=[i+j for j in range(3) for i in range(2,5)]
print(lst3)

lst4=[[a+b for b in range(2,6)] for a in range(4)]
print(lst4)

lst5=[(p,q) for p in range(1,3) for q in range(1,3)]
print(lst5)