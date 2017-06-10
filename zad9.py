a,b,c,d=int(input()),int(input()),int(input()),int(input())
print(end='')
for i in range(a,b+1):
    print('\t',i, end='')
print()
for j in range(c,d+1):
    print(j,end='')
    for i in range(a,b+1):
        print('\t',i*j,end='')
    print()