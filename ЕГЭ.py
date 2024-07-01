# Переводы чисел в разные системы исчисления
#number = 636
#transformation = bin(number)  # из десятичной системы счисления в двоичную
#print(transformation)
#transformation = oct(number) # из десятичной системы счисления в восьмеричную
#print(transformation)
#transformation = hex(number) # из десятичной системы счисления в шестнадцатеричную
#print(transformation)
#n = 636
#print(f'Двоичное: {n:b}') # указываем буквы b - для двоичной
#print(f'Восьмеричное: {n:o}') #  o - для восьмеричной
#print(f'Шестнадцатеричное: {n:x}') # x - для шестнадцатеричной системы счисления
#def F (g, e, k, t):
#    l1 = k and not g and t and e
#    l2 = not k and e and g and t
#    l3 = t and not e and g and not k
#    return int(l1 or l2 or l3)
#print('g, e, k, t | F(g, e, k, t)')
#for g in 0, 1:
#    for e in 0, 1:
#        for k in 0, 1:
#            for t in 0, 1:
#                if F(g, e, k, t) == 1:
#                    print(g, e, k, t, '   | ', F(g, e, k, t))
def f(n):
    bn = bin(n)[2:]
    print(bn)
    for i in bn:
        i = int(i)
        print(i)
        if i == 1:
            i += i
            print(i)
            if i % 2 == 0:
                bn = str(bn) + '00'
                return int(bn, 2)
            else:
                bn = str(bn) + '10'
                return int(bn, 2)
for n in range(1, 400):
    print(f(n))




