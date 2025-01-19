data = {}
nums = 0

nums = int(input('Enter the number of students: '))

for i in range(nums):
    name = input('Name: ')
    mark = int(input('Marks: '))

    data[name] = mark
    nums = nums - 1

# print(data)

while True:
    find_name =input('Enter Name for find marks: ')
    get_data = data.get(find_name)

    if get_data == None:
        print('Not found data')

    else :
        print('Marks : ', get_data)

    opt = input('Do you want to find another information [Yes | No]')

    if opt == 'No' or 'n':
        break

print('Thank you')