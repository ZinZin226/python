mylist = ['zin', 1, 2, 3]
print(mylist)
mylist.insert(1, 'win')
print(mylist)

mylist.reverse()
print(mylist)
mylist[1] = 'min'
print(mylist)

mylist[0:4] = mylist[0:4][::-1] #reverse index 1 to 3 only
print(mylist)

newlist = [4, 9, 7, 0]
newlist.sort()
print(newlist)

list2 = ['apple', 'pineapple', 'banana']
list2.sort()
print(list2)

list2.sort(key=len, reverse=True)
print(list2)

string1 = 'apple'
string2 = 'apple'
string3 = string1 is string2
print(string3)
print(id(string1), id(string2))

newlist1 = ['apple']
newlist2 = ['apple']
newlist3 = newlist1 is newlist2
print(newlist3)
print(id(newlist1), id(newlist2))