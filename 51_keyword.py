def data(name, age):
    print('Name : ', name)
    print('Age : ', age)

# positional arguments
data('Zin Zin', 20)

# default arguments
data(age=21, name='Min Khant')

# default arguments
def mydata(name, age=21):
    print('Name : ', name)
    print('Age : ', age)

mydata('zinzin')