mylist = ['zin', 'win', 1, 2, 3]
print(mylist)
mylist.append('min khant') #add end of the list
print(mylist)
newlist = ['han', 'lin', 'oo']
mylist.append(newlist)
print(mylist)
list2 = ['myat', 'thu']
mylist.extend(list2)
print(mylist)

list3 = ['bhone', 'thant']
mylist += list3 # same as extend  
print(mylist)