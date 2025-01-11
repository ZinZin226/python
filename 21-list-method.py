mylist = ['zin', 'win', 'han', 'lin', 'oo']
print(mylist)
mylist.remove('zin') #detail
print(mylist)
mylist.pop(3) # remove with index num
print(mylist)
print(mylist.index('lin')) # check index num
mylist.clear()
#del mylist
print(mylist)

list2 = ['min', 'khant', 1, 1, 2]
count = list2.count(2)
print(count)
print(f'1 in list2 is {count} time')
print(list2.count(1))