# key, value
dict1 = {}
print(dict1)
print(type(dict1))
 # dict => no index
dict1[10] = 'Min Khant'
dict1[20] = 'Han Lin Oo'
dict1[30] = 'Zin Zin Win Htet'

print(dict1)

dict2 = {'name': 'Zin Zin Win Htet', 'roll' : 2, 'major' : 'Mechatronics'}
print(dict2)
print(dict2.keys())
print(dict2.values())
print(dict2['roll'])

for key,value in dict2.items():
    print(key, value)


# n = input('Enter name: ')
# r = int(input('Enter roll: '))
# m = input('Enter major: ')

# dict3={'Name' : n, 'Roll' : r, 'Major' : m}
# print(dict3)

#progaram 
# Name  Roll  Major
# Zin   2     Mechatronics
data = {}
nums = 0

nums = int(input('Enter the number of students: '))

while nums > 0:
    name = input('Name: ')
    roll = int(input('Roll: '))

    data[name] = roll
    nums = nums - 1

# print(data)
print('Name\t\tRoll')


for key,value in data.items():
    print(key, '\t', value)