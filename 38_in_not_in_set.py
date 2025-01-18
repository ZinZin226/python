set1={'zinzin', 'minkhant', 'hanlinoo'}
print(set1)
print(type(set1))

set2=set('minkhantaungsoe')
print(set2)
print(type(set2))

for i in set('minkhantaungsoe'):
    print(i)

set3=set('zinzin')
print('h' in set3)
print('z' in set3)
print('k' not in set3)

# program
list1=[1, 1, 1, 3, 3, 2, 1, 7, 7, 8, 9]
set1= set(list1)
print(set1)

# program
name=input('Enter string : ')
string=set('a, e, i, o, u')
print(string.intersection(name))