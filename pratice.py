# print("Hello World")

# a = 18
# b = 24
# print (f'A is {a} B is {b}')
# print ('A is {} B is {}' . format(a, b))
# print ('Hello {1}, from {0} Hmawbi {2}' . format('mechatronics', 'Zin Zin', 'TU'))
# print ("Hello {name}, the age is {age}" . format(name='Zin Zin', age='21'))
# print ("Hi {love}, we have been loved for {time}." . format(love='Min Khant Aung Soe', time='2yrs 1mth 3dys'))

# c = 19.636
# name = 'Zin Zin'
# print ('the value of c is %.1f' %c )
# print ('My name is ',name)
# print ( 18 + 5)

# d = '35'
# print (type(d), d)
# e = int(d)
# print (type(e), e)
# f = float(3)
# print (type(f), f)
# com = 1j
# print (com)

# num = 33
# my_complex = complex(num)
# print (my_complex)
# print (type(my_complex))

# i = k = h = 366
# print (i, k, h)
# x, y, z = "X", "Y", "Z"
# print (x, y, z)

# fruits = ["apple", "banana", "avocado"]
# t, u, v = fruits
# print (t, u, v)
# print ( t, v)
# print ( u)

# num = 24E4
# print (num)
# print ( 3**2)

# a = 10
# b = 20
# c = 10
# if a == b:
#     print ('a is equal b')
# elif a ==c:
#     print('a is equal c')
# else:
#     print('a is neither b nor c')

mylist = ['min', 'khant', 7, 2, 9]
print(mylist)
print(mylist[1])
mylist.insert(2, ['aung', 'soe'])
print(mylist)
print(mylist[2][0], mylist[3])
mylist.append('zin')
print(mylist)
mylist.remove(2)
print(mylist)
mylist.pop(4)
print(mylist)
mylist.clear()
print(mylist)
# del mylist
mylist1 = ['zin', 'zin']
print(mylist1)
list1 = ['aung', 'soe']
mylist1.extend(list1)
print(mylist1)
list2 = [2, 5, 8, 4, 0]
mylist1 += list2
print(mylist1)
newlist = ['min', 'khant', 'aung', 'soe']
mylist1.append(newlist)
print(mylist1)
print(mylist1.index('aung'))
count = mylist1.count('soe')
print(count)
print(mylist1.count('aung'))