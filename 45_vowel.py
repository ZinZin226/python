string = input('Enter string: ')
vowel = {'a', 'e', 'i', 'o', 'u'}
data = {}

for i in string:
    if i in vowel:
        data[i] = data.get(i, 0)+1

# print(data)

for key, value in sorted(data.items()):
    print(key, '==>', value, 'times')