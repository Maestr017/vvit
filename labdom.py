from math import sqrt
a = float(input())
b = float(input())
c = float(input())
D = b**2 - 4*a*c
if a != 0 and b != 0 and c != 0:
    if D < 0:
        print('нет корней')
    if D == 0:
        print(-b/2*a)
    if D > 0:
        print(((-b + sqrt(D)) / (2*a)), ((-b - sqrt(D)) / (2*a)))
if a == 0 and b == 0 and c != 0:
    print('не определено')
if a == 0 and b != 0 and c != 0:
    print(-c/b)
if a != 0 and b == 0 and c != 0:
    if (c < 0 and a > 0) or (c > 0 and a < 0):
        print(sqrt(-c/a), -sqrt(-c/a))
    else:
        print('нет корней')
if a!= 0 and b != 0 and c == 0:
    print(0, -b/a)
if (a == 0 and b == 0 and c == 0) or (a == 0 and b != 0 and c == 0) or (a != 0 and b == 0 and c == 0):
    print(0)