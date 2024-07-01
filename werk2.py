#1. Составить матрицу размером 3х3 из случайных чисел от 0 до 15.
#2. Найдите максимальную элемент этой матрицу.
#3. Увеличить каждый элемент матрицы на этот элемент.
import random
x = 0
matrix1 = [[x, x, x], [x, x, x], [x, x, x]]
matrix2 = [[], [], []]
for r in range(len(matrix1)):
    text = ''
    for k in range(len(matrix1[r])):
        for i in range(0, 9):
            i = random.randint(0, 15)
        x = matrix1[r][k] + i
        matrix2[k].append(x)
        text += str(x) + ' '
    print(text)
list_1 = []
for i in range(len(matrix2)):
    for k in range(len(matrix2)):
        matrix2[i][k] = int(matrix2[i][k])
        list_1.append(matrix2[i][k])
max_1 = max(list_1)
print("\t", max_1)
for r in range(len(matrix2)):
    text_2 = ''
    for k in range(len(matrix2[r])):
        matrix2[r][k] = (matrix2[r][k] * max_1)
        text_2 += str(matrix2[r][k]) + ' '
    print(text_2)

# Напишите функцию для определения наибольшего числа в списке. Без использования max().
def bol(a):
    a = str(a)
    w = a[0]
    for i in range(1, len(a) - 1):
        if a[i] > w:
            w = a[i]
    return w
vvod = int(input())
print(bol(vvod))

# Напишите функцию, которая принимает на вход список строк и возвращает список строк,
# содержащих только уникальные символы.
w = input()
e = input()
r = input()
t = input()
y = [w, e, r, t]
def G(y):
    p = []
    u = 0
    for i in range(u, len(y)):
        if y[i] in p:
            u += 1
        else:
            p.append(y[i])
    return p
print(G(y))
