set1={1, 1, 2, 3, 3, 5} #set is unique
print(set1)
print(type(set1))

list1=[1, 1, 2, 3, 4, 5, 6, 7]
print(list1)
print(type(list1))

set2=set(list1)
print(set2)
print(type(set2))

print('length of set', len(set2))
print('length of list', len(list1))

set3=set(range(6))
print(set3)

set4=set(i for i in range(5))
print(set4)
