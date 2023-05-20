t = 0
g = 9.8
x = 0
v = 0
a = 0
b = 0
c = 0
d = 0
e = 0
while t < 10:
    t = t + 0.000068
    x = 0.5 * g * t**2
    if x < 100:
        a = "o"
    else:
        a = "#"
    if 100 < x < 200:
        b = "o"
    else:
        b = "#"
    if 200 < x < 300:
        c = "o"
    else:
        c = "#"
    if 300 < x < 400:
        d = "o"
    else:
        d = "#"
    if x > 400:
        e = "o"
    else:
        e = "#"
    print(a,b,c,d,e)