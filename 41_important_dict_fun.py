data = {1:'zin', 2:'min', 3:'han'}

# get data
print(data[3])
print(data.get(2))

#print(data[4])
print(data.get(4))
print(data.get(1, 'han'))
print(data.get(4, 'aung'))

# delete data
print(data.pop(2))
print(data)

data1 = data.copy()
print(data1)