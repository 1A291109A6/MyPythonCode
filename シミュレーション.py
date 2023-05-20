a = 5
b = 5

for i in range(10):
    ka = a
    kb = b
    a = kb /4
    b = ka + kb * 3 / 4
    print(a)
