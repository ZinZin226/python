# import random
from random import randint

ran_num1 = randint(0,9)
ran_num2 = randint(0,9)
money = 0
r_money = 0
win_money = 0
lose = True
r_win = False


lottery_num = str(ran_num1) + str(ran_num2) #change type for checking

lottery_list = []
unit = 0 # user add amount
usr_amount = 0

#check total lottery list = 0
total_bet = 0

#for money control
print('\n---------------------------------------------------')
print('       ------ Welcome to lottery bet -----     ')
print('---------------------------------------------------\n')
print('You can add at least 1000 or more')
unit = int(input('Enter the money want to add : '))

# 

if unit < 1000:
    unit = 0
    print('Please add at least one thousand(1000)')
else:
    usr_amount += unit
    print('Now your balance is : ', unit)
    total_lot = int(input('Enter total number of lottery: '))

#Show Bet money and user amount
    def showBetAndAmount(total_bet, usr_amount):
        print('\n--------------------------------------------')
        print(f'Total bet {total_bet} units')
        print('Now your balance is : ', usr_amount)


    #check for total list
    while total_lot != 0:

        if usr_amount <=0 :
            break

        print('\n------------------------------------------')
        usr_name = str(input('Enter the lottery num: '))
        money = int(input('Enter the money want to bet: '))
        check_r = str(input('R ? '))
    
        if money > usr_amount:
            print('Not enough money')
            showBetAndAmount(total_bet , usr_amount)
            break
            

        lottery_list.append(usr_name)
    #check reverse or not
        if check_r.upper() == 'R':
            r_money = int(input('Enter the R money : '))
            temp = money
            money += r_money

    #add total bet and reduce amount        
            if money > usr_amount:
                print('Not enough money')
                showBetAndAmount(total_bet + temp, usr_amount - temp)
                break
            
            reverse_num = usr_name[::-1]
            lottery_list.append(reverse_num)

    #check if r_money is win or not
            for i in lottery_list:
                if (lottery_num == i):
                    lose = False
                    r_win = True
                    win_money = r_money * 80        
        else:
            reverse_num = 0

        usr_amount -= money # reduce user money
        total_bet += money
        total_lot -=1 #number of lottery

        #show total bet money
        showBetAndAmount(total_bet, usr_amount)
       

#show random lottery and check win or lose
print('Your lottery nums are: ', ','.join(lottery_list))

print('\n-------------------------------------------------------')

print(f"Today lottery number is {ran_num1}{ran_num2}")

print('--------------------------------------------------------\n')


for i in lottery_list:
    if (lottery_num == i):
        lose = False
        if r_win:
            temp = money * 80
            win_money = temp - win_money
            usr_amount = usr_amount + win_money
        else:
            win_money = money * 80
            usr_amount = usr_amount + win_money

        print(f'You win {win_money} ^-^')
        print('Now your money is ', usr_amount)
    else:
        if lose == False:
            lose = False
        else:
            lose = True
if lose:
    print('You lose your money ~_~" \n')