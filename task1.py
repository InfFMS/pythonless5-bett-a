# Заполните список длины N случайными числами в диапазоне от 0 до 1000
# Выведите:
# 1.длину списка;
# 2.последний элемент списка;
# 3.список в обратном порядке (вспоминаем срезы);
# 4.YES, если список содержит трехзначное число, состоящее из одинаковых цифр
# NO в противном случае;
# 5.список с удаленными первым и последним элементами.

from random import randint

def find(x):
    for i in x:
        if 100 <= i <= 999:
            if i % 10 == i // 100 and i % 10 == (i // 10 % 10):
                return True
    return False

n = int(input())
lst = [randint(0, 1000) for _ in range(n)]
#print(lst)

print(len(lst))
print(lst[-1])
print(lst[::-1])
if find(lst):
    print('YES')
else:
    print('NO')

lst.pop(0)
lst.pop(-1)
print(lst)


