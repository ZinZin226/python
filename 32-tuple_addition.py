tuple1 = (10, 20, 30)
tuple2 = (1, 2, 3)
tuple1 += tuple2
print (tuple1)

# Repitition Operator (*)
tuple_ = (100, 200)
tuple_ *= 3
print (tuple_)

print('length of tuple_', len(tuple_))
print('count :' , tuple_.count(100))
print('index : ', tuple_.index(200))

my_tuple = (400, 200, 700, 100)
print (my_tuple)
sorted_tuple = sorted(my_tuple)
print(sorted_tuple)
reverse_tuple = sorted(my_tuple, reverse = True)
print(sorted_tuple)
print(type(sorted_tuple))

print('Minimun value in my_tuple : ',min(my_tuple))
print('Maximun value in my_tuple : ', max(my_tuple))
