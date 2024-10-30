# При анализе данных, собранных в рамках научного эксперимента,
# бывает полезно удалить самое большое и самое маленькое значение.
# Сымитруем данные списком длины N со случайными числами в диапазоне от 0 до 1000
# Удалите из этого списка все значения, которые на 30 % отличаются
# от среднего значения списка

import random
lst = [random.randint(0, 1000) for _ in range(int(input()))]
new_lst = list()
arithmetic_mean = sum(lst)/len(lst)
dif = 0.3 * arithmetic_mean

for i in lst:
    if arithmetic_mean - dif <= i <= arithmetic_mean + dif:
        new_lst.append(i)

print(lst)
print(new_lst)