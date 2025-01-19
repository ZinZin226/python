data = {1:'Zin ZIn', 2:'Han Lin', 3:'Min Khant'}
print(data)

print(data.popitem())
print(data)

# data2 = {}
# print(data2.popitem())

data3 = {'name': 'Zin Zin', 'age': 21, 'school': 'TU'}

#get only keys
for key in data3.keys():
    print(key)

#get only values
for value in data3.values():
    print(value)

# get both keys, values
for key, value in data3.items():
    print(key, value)