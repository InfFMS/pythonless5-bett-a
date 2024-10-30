# Заполнить массив длины N случайными числами в диапазоне от 10 до 100000 и
# отобрать в другой массив все числа, которые состоят из одинаковых цифр.
# Используйте для этого логическую функцию.
# Пример: ввод N = 4
# [12, 77, 5555, 97]
# Вывод: [77, 5555]

import random

def find(x):
    x = list(str(x))
    for i in range(len(x) - 1):
        if x[i] != x[i + 1]:
            return False
    return True

lst = [random.randint(0, 100000) for _ in range(int(input()))]
new_lst = list()

for j in range(len(lst)):
    y = lst[j]
    if find(y):
        new_lst.append(y)

print(lst)
print(new_lst)