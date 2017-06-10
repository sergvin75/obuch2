a = int(input())
b = int(input())
c = int(input())
if (a >= b) and (b >= c):
    print(a)
    print(c)
    print(b)
elif (c >= a) and (a >= b):
    print(c)
    print(b)
    print(a)
elif (b >= a) and (a >= c):
    print(b)
    print(c)
    print(a)
elif (c >= b) and (b >= a):
    print(c)
    print(a)
    print(b)
elif (b >= c) and (c >= a):
    print(b)
    print(a)
    print(c)
elif (a >= c) and (c >= b):
    print(a)
    print(b)
    print(c)