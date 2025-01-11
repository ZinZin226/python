from random import randint

ran_num1 = randint(0,9)
ran_num2 = randint(0,9)

lottery_num = str(ran_num1) + str(ran_num2)

ur_num = int(input('Enter your lottery num: '))

print('\n-------------------------------------')
print('Today lottery number is' , lottery_num)
print('-------------------------------------\n')

print('Your lottery num is ', ur_num)

if ur_num == lottery_num:
    print('You win the lottery ^-^')
else:
    print('You Lose! Good luck next time -_-')