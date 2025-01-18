#pack
a = 10
b = 20
c = 30
d = 40

tuple_ = a, b, c, d
print(tuple_)
print(type(tuple_))

#unpack
tuple1= (1, 2, 3, 4)
a, b, c, d = tuple1
print(a, b, c, d)

#comprehension
#comperhension in list

list_ = [i for i in range(6)]
print(list_)

tuple1 = (i for i in range(6)) # Just only tuple shows address
print(tuple1)

for i in tuple1:
    print(i)