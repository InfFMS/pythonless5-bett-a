# Посчитайте угол между двумя векторами размерности N.
# Примечание: Вспомните определение скалярного произведения.
# Изначально вектор заполните рандомными числами.
# Пример: N =3
# вектор a = [0, 1, 0]
# вектор b = [1, 0, 0]
# Угол = 90

import random
import math

def find_mod(lst):
    x = lst[0]
    y = lst[1]
    z = lst[2]
    m = math.sqrt(x**2 + y**2 + z**2)
    return m

def rad_to_grad(x):
    grad = x / (math.pi /180)
    return grad
A = [random.randint(-10, 10) for _ in range(3)]
B = [random.randint(-10, 10) for _ in range(3)]

s = A[0] * B[0] + A[1] * B[1] + A[2] * B[2]
m1 = find_mod(A)
m2 = find_mod(B)

cos = s/(m1 * m2)
print(cos)
print(rad_to_grad(math.acos(cos)))


