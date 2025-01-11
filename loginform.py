user_name = 'zinzin'
user_password = 1234
counter = 0

while counter < 2:
    name = input('Enter your name: ')
    password = int(input('Password: '))
    if name == user_name and password == user_password:
       print('Login success')
       break
    else:
       print('Login fail')
       counter +=1
       if counter == 2:
          print('Sorry, Try Again!!')
               