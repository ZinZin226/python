def add(num1, num2):
    return(num1 + num2)

num = 2
num2 = num + add(2, 5)
print(num2)


def printName():
    print('Zin Zin')
    return 1

printName()
print(printName()) #  give both funaction and return value ( no return => none(default value))
