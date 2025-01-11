print ('Hello World')

#format
a = 10
b = 11
print ("A is {} B is {}".format(a,b))
print (f'A is {a} B is {b}')
print ("Hello {2} from {0} , I'm {1}.".format('Mechatronics', 'Zin Zin', 'Freshers'))
print ("Hello guys!! My name is {name} and I'm {age} years old".format(name='Zin Zin' , age = 21))

c = 12.3456
name = "Teddy"
print ('The value of c is %.2f'%c)
print ('My love is ', name)
print ( 10+5 )

d = '24'
print (type(d), d)
e = int(d)
print (type(e), e)
f = float(7)
print (type(f), f)

com = -4j

print (type(com), com)

num = 22
my_complex = complex(num)
print (my_complex)
print (type(my_complex))

a=b=c= 35
print ( a, b, c)
x , y , z = "X", "Y", "Z"
print (x,y,z)
Fruits = ["Apple", "Banana", "Avocado"]
x, y, z = Fruits
print (x, y, z)
print (z)

num = 24E4
print (num)
print (2**8)
print (range(6))

name = "zin zin"
print (name.upper())
print (name.capitalize())
print (name.lower())

print (name.strip()) 

print (len(name))

u = bool(1)
u1 = bool([])
u2 = bool({})
u3 = bool(())
u4 = bool(False)
u5 = bool(None)
u6 = bool(0)
u7 = bool("")
u8 = bool('')
print (u, u1, u2, u3, u4, u5, u6, u7, u8)

name = input('Enter your name: ')
age = int(input('Enter your age: '))
print (f'Your name is {name} and your age is {age}.')

name = 'Zin Zin'
age = 21
# del [name, age] 
print (name)
print (age)

x = 12
y = 34
num = x + y
print (num)

name = 'Zin Zin'
print (name.isupper())
print (name.islower())
print (name.count('z'))
print (name.count('i'))
print (name.find('n'))
print (name.replace('Zin', 'zin'))

a = 2+5
b = 8-3
c = 3*6
d = 6/2
e = 3**5
f = 25//2
g = 9 % 5
print (a, b, c, d, e, f, g)

m = 65
n = 24
print (m > n)
print (m < n)
print (m >= n)
print (m <= n)
print (m != n)
print (m == n)

j = 10
k = 10
i = 34
l = 58
print (j == k and i != l)
print (j == k or i != l)
print (j != k or i != l)
print (j != k and i != l)

print (i & l)
print (i | j)
print (i ^ l)
print (j ^ k)

i +=6
print (i)

print (id(j))
print (id(k))
print (id(i))
print (j is k)
print (j is not k)
print (i is not l)
print (i is l)

name = "teddy"
print ('m' in name)
print ('m' not in name)

a = 10
b = 20
c = 10
if a == b:
    print ("a is equal b")
elif a == c:
    print ("a is equal c")
else:
    print ("a is neither b bor c")

mylist = ['zin', 'zin', 'teddy', 1, 7, 9]
a, b, c, d, e, f = mylist
print (mylist)
print (e)
print (mylist[2])

mylist2 = ['jk', 'v', 'tae', ['bts', 'twice'], 5, 8, 2]
print (mylist2[3][0])

mylist3 = ['oo', 'tt', 'zz', ['ww', 'uu', 1, 4, 8, ['love'], ['gg', 'kk', 3, 9, 0]], 23 ]
print (mylist3[3][1])
print (mylist3[3][5])
print (mylist3[3][6][2])

print (mylist2)
mylist2.remove(8)
print (mylist2)
mylist2.pop(4) 
print (mylist2)
print (mylist2.index('v'))
mylist2.clear()
print (mylist2)
# del mylist2
print (mylist2)

list2 = ['min', 'khant', 1, 6, 'min', 'min']
count = list2.count('min')
print (count)
print (f'min in list2 is {count} times')
print (list2.count(1))

list2.append ('aung')
print (list2)
newlist = ['soe', 22]
list2.append(newlist)
print (list2)
list2.extend(newlist)
print (list2)

newlist2 = ['zin', 'zin']
list2 += newlist2
print (list2)