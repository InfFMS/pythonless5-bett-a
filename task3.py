# Заполните массив длины N случайными числами в интервале [0,100].
# Определить, есть ли в нем элементы с одинаковыми значениями,
# не обязательно стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 6
# [1, 2, 3, 2, 5, 10]
# Вывод:
# значение:2 индексы 1 и 3


import random

value = list()
index = list()
lst = [random.randint(0, 100) for _ in range(int(input()))]
print(lst)
def find_all_index(lst, x):
    indx = list()
    for i in range(len(lst)):
        if lst[i] == x:
            indx.append(i)
    return indx

def check_repeats(lst):
    for i in lst:
        if len(i) > 1:
            return False
    return True

for i in range(len(lst)):
    q = lst[i]
    if q not in value:
        value.append(q)
        index.append(find_all_index(lst, q))


for j in range(len(value)):
    if len(index[j]) < 2:
        continue
    else:
        print(f'значение: {value[j]} индексы:',*index[j])

if check_repeats(index):
    print('NO')




#print(value)
#print(index)
#print(find_all_index(lst, 0))


