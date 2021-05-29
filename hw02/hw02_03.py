def invert_number(number):
    #print(number)
    if number // 10 <= 0:
        return str(number)
    return str(number % 10) + invert_number(number//10)


def input_number():
    try:
        number = int(input('Введите число: '))
        return number
    except ValueError:
        print('я работаю только с целыми положительными числами')
        return input_number()


print(invert_number(input_number()))

