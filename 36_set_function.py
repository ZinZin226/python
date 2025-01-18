set1= {1, 2, 4, 6, 7, 9}  # set no duplicate

print(set1)

#add function
set1.add(0)
print(set1)

set1.add(3)
print(set1)

set1.add(10)
print(set1)

#print(set1[1])#set => no index

# update
list1=[1, 2, 4, 7, 7, 9, 3]
set2={1, 2, 3, 4, 5, 6, 7, 8}

set2.update(list1, set2)
print(set2)

set3={ 2+ 3 }
print(set3)

# copy
print('set 1 ', set1)
set3=set1.copy()
print('set 3 ', set3)

# pop => delete for only first one
set4={4, 2, 3, 1, 5} # 1 2 3 4 5
set4.pop() # 1
print(set4.pop()) # 2
print(set4)

# remove
set5={4, 5, 2, 1, 6}
print('set 5 ', set5)
set5.remove(4)
print('set 5 ', set5)

# discard
set6=set5.copy()
print('set 6 ', set6)
set6.discard(6)
print('set 6 ', set6)
set6.discard(3)
print('set 6 ', set6)

set6.clear()
print('set 6 ', set6)