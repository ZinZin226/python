from random import randint

ran_num1 = randint(0,9)
ran_num2 = randint(0,9)


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

if unit < 1000:
    unit = 0
    print('Please add at least one thousand(1000)')
else:
    usr_amount += unit
    print('Now your balance is : ', unit)
    total_lot = int(input('Enter total number of lottery: '))



    #check for total list
    while total_lot != 0:
        if usr_amount ==0:
            print('Not enough money')
            break

        print('\n------------------------------------------')
        money = int(input('Enter the money want to bet: '))
        usr_name = str(input('Enter the lottery num: '))
        check_r = str(input('R ? '))

        lottery_list.append(usr_name)
    #check reverse or not
        if check_r.upper() == 'R':
            r_money = int(input('Enter the R money : '))
            money += r_money
            
            reverse_num = usr_name[::-1]
            lottery_list.append(reverse_num)
        else:
            reverse_num = 0

        usr_amount -= money # reduce your money
        total_bet += money
        
        total_lot -=1 #number of lottery

        #show total bet money
        print('\n--------------------------------------------')
        print(f'Total bet {total_bet} units')
        print('Now your balance is : ', usr_amount)
