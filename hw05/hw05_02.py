class HexNumber:
    def __init__(self, number):
        self.number_list = list(self.number_check(number).upper())

    @staticmethod
    def number_check(number):
        try:
            int(number, 16)
            return number
        except ValueError:
            print('Некорректный ввод числа! Будем считать, что вы ввели "0"')
            return '0'

    def __mul__(self, other):
        try:
            return list(hex(int(''.join(self.number_list), 16) * int(''.join(other.number_list), 16)).upper()[2:])
        except TypeError:
            print('Ошибка вычисления')
            return None

    def __add__(self, other):
        try:
            return list(hex(int(''.join(self.number_list), 16) + int(''.join(other.number_list), 16)).upper()[2:])
        except TypeError:
            print('Ошибка вычисления')
            return None


#first_num = HexNumber(input('Введите число в шестнадцатеричном формате: '))
#second_num = HexNumber(input('Введите число в шестнадцатеричном формате: '))


first_num = HexNumber('A2')
second_num = HexNumber('c4f')

print(f'Первое число: {first_num.number_list}')
print(f'Второе число: {second_num.number_list}')

print('Сумма: ', first_num + second_num)
print('Произведение: ', first_num * second_num)
