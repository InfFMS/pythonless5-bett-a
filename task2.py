# Заполните массив длины N случайными числами в интервале [0,5].
# Определить, есть ли в нем элементы с одинаковыми значениями, стоящие рядом.
# Если есть, то выведете значение и индекс повторяющихся элементов
# Если нет, то написать "Нет"
# Пример: ввод N = 7
# [1, 2, 3, 3, 2, 2, 1]
# Вывод:
# значение:3 индексы 2 и 3
# значение:2 индексы 4 и 5

import random

value = list()
index = list()
lst = [random.randint(0, 5) for _ in range(int(input()))]
print(lst)
for i in range(len(lst) - 1):
    f = lst[i]
    s = lst[i + 1]
    if f == s:
        value.append(lst[i])
        index.append([i, i + 1])

for j in range(len(value)):
    print(f'значение:{value[j]} индексы: {index[j][0]} и {index[j][1]}')