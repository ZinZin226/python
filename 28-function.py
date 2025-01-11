#normal function
def test():
    print('I am test')

test()

#parm pass

def name(my_name):
    print('My name is ', my_name)

name('Zin Zin')

#parm default
def add(first, second=3):
    print(first + second)

add(2 , 4)