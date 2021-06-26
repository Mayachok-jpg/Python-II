from collections import namedtuple


def input_data():
    company = namedtuple('company', 'name quarter_1 quarter_2 quarter_3 quarter_4 profit_sum')
    name = input('Введите название предприятия: ').rstrip()
    while True:
        try:
            profit = list(map(int, input('Введите прибыль предприятия за каждый квартал (через пробел):').split()))
        except ValueError:
            print('Вы ввели некорректные данные')
        else:
            if len(profit) != 4:
                print('Необходимо ввести прибыль за каждый квартал (4 значения).')
            else:
                break
    return company._make([name, *profit, sum(profit)])


def average_profit_count(firm_list: list):
    try:
        avg_profit = sum([getattr(company, 'profit_sum') for company in firm_list]) / len(firm_list)
        print(f'Средняя годовая прибыль: {avg_profit}')
        return avg_profit
    except ZeroDivisionError:
        print('Вы не внесли данных')
        return None


def firms_statistics(firm_list, profit):
    if profit is None:
        print('Нечего считать')
    else:
        less_then_average = []
        more_then_average = []
        for company in firm_list:
            if company.profit_sum >= profit:
                more_then_average.append(company.name)
            else:
                less_then_average.append(company.name)
        print(f'Предприятия с прибылью выше среднего значения: {", ".join(more_then_average)}')
        print(f'Предприятия с прибылью ниже среднего значения: {", ".join(less_then_average)}')


counter = int(input('Введите количество предприятий для расчета прибыли: '))
firms = [input_data() for i in range(counter)]

average_profit = average_profit_count(firms)
firms_statistics(firms, average_profit)