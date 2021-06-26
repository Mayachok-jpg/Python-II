class StackClass:
    def __init__(self, size):
        self.elems = [[]]
        self.size = size  # размер стопки. Для отладки лучше маленький

    def is_empty(self):
        return self.elems == [[]]

    def push_in(self, el):
        i = len(self.elems) - 1
        j = len(self.elems[i]) - 1 if len(self.elems[i]) > 0 else 0
        if j >= self.size - 1:
            #print('стопка заполнена!')   #для отладки
            self.elems.append([])
            self.elems[i+1].append(el)
        else:
            self.elems[i].append(el)
        #print(self.elems)  #выводила для отладки

    def pop_out(self):
        i = len(self.elems) - 1
        j = len(self.elems[i]) - 1 if len(self.elems[i]) > 0 else 0
        #print('удаление')
        print(self.elems)
        if j == 0:
            #print('Последний элемент в стопке')
            #print(self.elems)    #для отладки
            last_el = self.elems[i].pop()
            self.elems.pop()
            return last_el
        else:
            #print(self.elems)   #для отладки
            return self.elems[i].pop()

    def get_val(self):
        i = len(self.elems) - 1
        j = len(self.elems[i]) - 1 if len(self.elems[i]) > 0 else 0
        return self.elems[i][j]

    def get_mid_val(self, num):  # взять верхний элемент из не последней стопки
        i = num - 1
        j = len(self.elems[i]) - 1 if len(self.elems[i]) > 0 else 0
        return self.elems[i][j]


    def stack_size(self):
        i = len(self.elems) - 1
        return i*self.size + len(self.elems[i])

    def stack_num(self):   # количество стопок
        i = len(self.elems) if not self.is_empty() else 0;
        return i


if __name__ == '__main__':

    SC_OBJ = StackClass(3)

    print(SC_OBJ.is_empty())  # -> стек пустой
    print(f'Количество стопок: {SC_OBJ.stack_num()}')
    # наполняем стек
    SC_OBJ.push_in(10)
    SC_OBJ.push_in('code')
    SC_OBJ.push_in(False)
    SC_OBJ.push_in(5.5)
    # получаем значение первого элемента с вершины стека, но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())  # -> 5.5

    # узнаем размер стека
    print(SC_OBJ.stack_size())  # -> 4

    print(SC_OBJ.is_empty())  # -> стек уже непустой

    # кладем еще один элемент в стек
    SC_OBJ.push_in(4.4)
    print(f'Количество стопок: {SC_OBJ.stack_num()}')
    print(f'Элемент из 1 стопки: {SC_OBJ.get_mid_val(1)}')
    print(f'Элемент из 2 стопки: {SC_OBJ.get_mid_val(2)}')
    # убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 4.4

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())  # -> 5.5

    # вновь узнаем размер стека
    print(SC_OBJ.stack_size())  # -> 3
