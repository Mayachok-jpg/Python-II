def calculate():
    try:
        operation = input('Введите операцию (+, -, *, /) или 0 для выхода: ')
        if operation == '0':
            print('выход')
        else:
            if operation not in ['+','-', '*', '/']:
                raise ValueError
            else:
                try:
                    a = int(input('Введите первое число: '))
                    b = int(input('Введите второе число: '))
                except ValueError:
                    print('Строка вместо числа :( Теперь придется начинать с начала')
                    calculate()
                if operation == '+':
                    print(a + b)
                elif operation == '-':
                    print(a - b)
                elif operation == '*':
                    print(a * b)
                else:
                    try:
                        print(a / b)
                    except ZeroDivisionError:
                        print('Деление на ноль! D:')
                        #calculate()
                calculate()
    except ValueError:
            print('Недопустимый ввод')
            calculate()


print('Hello')
calculate()
print('Bye!')
