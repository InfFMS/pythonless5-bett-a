# Заполнить массив длины N случайными числами в интервале [-100,100] и
# переставить элементы так, чтобы все положительные элементы
# стояли в начала массива, а все отрицательные и нули в конце.
# Пример: ввод N = 6
# [20, -90, 15, -34, 10, 0]
# Вывод: [20, 15, 10, -90, -34, 0]

import random

lst = [random.randint(-100, 100) for _ in range(int(input()))]
print(lst)
pos = []
neg = []
zero = 0
for i in lst:
    if i == 0:
        zero += 1
    elif i > 0:
        pos.append(i)
    else:
        neg.append(i)

lst = pos + neg + [0] * zero
print(lst)