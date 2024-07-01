import random

def rendom_vord():
    a = [['слон', 'больльшое животное'], ['кошка', 'животное с вертикальными зрачками'],
         ['собака', 'дружелюбное животное'], ['айболит', 'лечит животных в сказке']]
    u = random.randint(0, len(a) - 1)
    print(a[u][1])
    return a[u][0]

def pal(r):
    o = []
    for i in range(0, len(r)):
        o.append('_')
    return o

r = rendom_vord()
a = pal(r)
print(' '.join(a))

def ottdel():
    k = 5
    list_1 = ''
    while True:
        p = input('Введите букву: ')
        flag = False
        for i in range(0, len(a)):
            if p == r[i]:
                list_1 += p
                a[i] = p
                print(' '.join(a))
                flag = True
        if flag == False:
            k -= 1
            print('у вос остолось ', k, 'жизней')

        if k == 0:
            print('казнен')
            break
        if len(list_1) == len(r):
            print(r, 'спасен')
            break