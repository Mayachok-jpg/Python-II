even = 0
odd = 0


def even_odd(number):
    global even, odd
    if (number % 10)%2 == 0:
        even += 1
    else:
        odd += 1
    number = number//10

    if number > 0:
        even_odd(number)
        #print(number, even, odd)
    return even, odd


def input_number():
    try:
        number = int(input('Введите число: '))
        if number == 0:
            raise ValueError
        return number
    except ValueError:
        print('я работаю только с целыми положительными числами')
        return input_number()


even, odd = even_odd(input_number())
print(f'Четных {even}, нечетных {odd}')

