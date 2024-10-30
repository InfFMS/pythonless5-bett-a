# Напишите программу, которая удаляет дубликаты из списка длины N.
# Пример работы:
# Пример: ввод N = 8
# [10, 20, 10, 20, 30, 40, 30, 50]
# После удаления дублей:  [10, 20, 30, 40, 50]

import random
lst = [random.randint(0,50) for _ in range(int(input()))]
new_lst = []
for i in lst:
    if not(i in new_lst):
        new_lst.append(i)

print(lst)
print(new_lst)