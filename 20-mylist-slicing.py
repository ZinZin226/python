mylist = ['zin', 'zin', 1, 2, 3]
a, b, c, d, e = mylist #unpack
print(mylist)
print(b)
print(mylist[1])

mylist2 = ['han', 'lin', ['oo', 'zin'], 'win', 'htet'] #list slicing
print(mylist2[2][1])

mylist3 = ['han', 'lin', ['oo', 'zin', ['htet'], ['min', 'khant']]]
print(mylist3[2][3][1])
print(mylist3[2][2])