def printab(a, b, *args):
    print(a)
    print(b)
    for arg in args:
        print(arg)

printab(10, 20, 30, 40, 50)
