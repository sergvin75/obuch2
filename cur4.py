def printab(a,b):
    print(a)
    print(b)

printab(10,20)

lst = [10,20]
printab(*lst)
args = {'a':10, 'b':20}
printab(**args)
