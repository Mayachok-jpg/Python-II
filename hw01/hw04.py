users = {'kate': ('kate123', True), 'max': ('#$@', False), 'polly': ('pI84', True), 'sofia': ('sorry', True)}


def check_activation(user):  # O(1)
    if users[user][1]:
        return True
    else:
        print('Необходимо пройти активацию')


def check_activation_2(checking_user):   #O(N)
    activated_users = [user for user in users if users[user][1]]
    if checking_user in activated_users:
        return True
    else:
        print('Необходимо пройти активацию')


def autorization(login, password):
    if password != users[login][0]:
        print ("неверный пароль")
    elif check_activation(login):
        print('доступ разрешен')


# check_activation('kate');
# check_activation('max');

#check_activation_2('kate');
#check_activation_2('max');

login = input('Введите логин: ')
password = input('Введите пароль: ')

autorization(login, password)

'''Первое решение эффективнее, проверяется только один элемент словаря, сложность константная.
Во втором перебирается весь словарь и генерируется новая структура данных, сложность зависит от 
количества пользователей'''

