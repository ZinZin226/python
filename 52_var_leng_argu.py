#variable length arguments

def nums(*num):
    print(num)

nums('Zin Zin', 20, 'Mechatronics')


def add(*nums):
    result = 0
    for num in nums:
        result += num
    # print(sum(nums))
    
    return result # cannot write anything under return (return => out function)

print(add(10, 20, 30, 40))