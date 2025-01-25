def check(num):
    if num % 2 == 0:
        print('even-number: ', num)
    else:
        print('odd-number: ', num)

check(68)
check(59)

# write a user-defined function to identify the factorial of a given range of numbers. (5! = 5 * 4 * 3 * 2 * 1)
def factorial(num):
    
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(5))
print(factorial(0))

# Write a program that calculates the addition and subtraction of two numbers

def calculate(num1 , num2):
    add = num1 + num2
    sub = num1 - num2
    return add, sub
    
addition, subtraction = calculate(5, 4)
print('Addition : ', addition)
print('Subtraction : ', subtraction)

def cal(num1, num2):
    add = num1 + num2
    sub = num1 - num2
    multi = num1 * num2
    div = num1 / num2

    return add, sub, multi, div

results = cal(5, 4)
for result in results:
    print(result)