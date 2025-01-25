dict1 = {'name' : 'Zin Zin', 'age' : 20}
print('Before Update ' , dict1)
dict2 = {'age' : 21} ## key => exactly (must be) same

dict1.update(dict2)
print('After Update ' , dict1)

dict3 = {'name' : 'Min Khant', 'major' : 'Mechatronics'}
dict1.update(dict3)
print(dict1)

dictA = {'a' : 1 , 'b' : 2}
dictA.update([('a' , 2), ('b' , 3), ('c' , 4)])
print(dictA)

dictA.update(c=5 , d=6)
print(dictA)

dictA.update({'a' : 10, 'b' : 20, 'c' : 30})
print(dictA)