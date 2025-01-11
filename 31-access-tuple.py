#using index
tuple_ = ( 1, 2, 3, 4)
print (tuple_[3])

list_ = [10, 20, 30, 40]
print (list_[2:30])
print (tuple_[2:30])

print(tuple_[30]) # Error: index out of range

#immutable 
list_[3] = 35
print(list_)

# tuple cannot add or delete elements
# tuple_[2] = 60
# print(tuple_)