from math import sqrt


def get_answer_1(a, c):
    a = float(a)
    c = float(c)
    return sqrt(a+c) + 1/(a+c)


def get_answer_2(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = b**2 - 4*a*c
    if D < 0:
        return 'None'
    if abs(D) < 0.0001:
        return ('x = {0:.2f}'.format(b / 2))
    x1 = (b - sqrt(D)) / 2
    x2 = (b + sqrt(D)) / 2

    return ('x1 = {}\nx2 = {}'.format(round(x1, 3), round(x2, 3)))


def get_answer_3(f, a, c, g):
    f = float(f)
    a = list(map(float, a.split()))
    c = list(map(float, c.split()))
    g = list(map(float, g.split()))

    for i in range(10):
        f += a[i]**2 + 56*c[i]*f*g[i]
    return 'F = {}'.format(round(f, 3))
