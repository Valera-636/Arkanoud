# С начала суток прошло n минут.
# Определите, сколько часов и минут будут показывать электронные часы в этот момент.
n = int(input())
hours = n % (60 * 24) // 60
minutes = n % 60
print(hours, minutes)

#
l = int(input("введите число: "))
k = "20 "
print(l * k)

for i in range(20, 51):
    if i % 5 != 0 and i % 3 == 0:
        print(i)

sum = 0
for i in range(100, 200):
    if i % 17 == 0:
        sum += i
print(sum)

# простые числа
for i in range(20, 200):
    e = 0
    for q in range(1, i + 1):
        if i % q == 0:
            e += 1
    if e == 2:
        print(i)

# Выводит все совершенные числа до 10000: число, равное сумме всех своих делителей, кроме себя самого
for i in range(1, 1000):
    q = 0
    for o in range(1, i):
        if i % o == 0:
            q += o
            if q == i:
                print('\t', q)
                q = 0

# Делимость чисел - кол-во делителей (+)
t = int(input('Введите число: '))
o = '+'
for i in range(1, t + 1):
    y = 0
    for q in range(1, i + 1):
        if i % q == 0:
            y += 1

    print(i, y * o)

# Вывадит числа Армстронга (153 = 1^3 + 5^3 + 3^3)
for i in range(10, 9999):
    q = 0
    w = len(str(i))
    for e in str(i):
        r = int(e)**w
        q += r
    if i == q:
        print(i)

# Удалить отрицательные числа из списка
e = [1, -4, 6, 90, -32, 8, -45]
for i in e:
    while i < 0:
        e.remove(i)
        break
print(e)

worke = ["Математики", "Физика", "Общество", "ИП"]
print(worke)
worke.insert(2, "Изо")
print(worke)
del worke[len(worke) - 1]
print(worke)

import random
x = random.randint(0, 255)
y = random.randint(0, 255)
z = random.randint(0, 255)
k = random.randint(0, 255)
print(str(x) + '.' + str(y) + '.' + str(z) + '.' + str(k))

# 
matrix1 = [[1,2,3], [4,5,6], [7,8,9]]
matrix2 = [[1,100,3], [412,5,6], [7,38,9]]
matrix3 = [[], [], []]
for i in range(len(matrix1)):
    text = ''
    for j in range(len(matrix1[i])):
        matrix3[i].append(matrix1[i][j] + matrix2[i][j])
        text += str(matrix3[i][j]) + ' '
    print(text)

# Найти мин элемент 3 ей строки и умножить его на все элементы матрицы
matrix1 = [[1,2,3], [4,5,6], [7,8,9]]
matrix3 = [[], [], []]
y = min(matrix1[2])
for i in range(len(matrix1)):
    tex = ''
    for q in range(len(matrix1[i])):
        matrix3[i].append(y * matrix1[i][q])
        tex += str(matrix3[i][q]) + ' '
    print(tex)
