#条件测试
car = 'subaru'
print("is car == 'subaru'? I predicted true")
print(car == 'subaru')
print("\nis car == 'audi'? I predicted false")
print(car == 'audi')

requested_guest = ['john','jane','kevin']
guest = 'john'
if guest in requested_guest:
    print('congrats! you are invited')
if guest not in requested_guest:
    print('sorry, you are not invited')

#if语句
alien_color = 'red'
if alien_color == 'green':
    print('you got 5 points!')
elif alien_color == 'yellow':
    print('you got 10 points!')
else:
    print('you got 15 points!')

age = 14
if age < 2:
    print('he is an infant')
elif age < 4:
    print('he is learning walking')
elif age < 13:
    print('he is a child')
elif age < 20:
    print('he is a teenager')
elif age < 65:
    print('he is an adult')
else:
    print('he is an old man')

#使用if语句处理列表
users = ['admin','john','jane','kevin']
for user in users:
    if user == 'admin':
        print('hello admin. would you like to see a status report?')
    else:
        print('hello '+user+', thank you for logging in again.')

users = []
if users:
    for user in users:
        if user == 'admin':
            print('hello admin, would you like to see a status report?')
        else:
            print('hello '+ user +', thank you for logging in again')
else:
    print('we need to find some user!')

current_users = ['john','kevin','admin']
new_users = ['john','jane']
for new_user in new_users:
    if new_user in current_users:
        print('sorry, this name is occupied!')
    else:
        print('you have set your name!')