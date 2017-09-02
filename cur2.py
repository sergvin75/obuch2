n=int(input())
if (n//10)%10 == 1:
    print (n,"программистов")
elif n%10 == 1:
    print (n," программист")
elif n%10 == 2 or n%10 ==3 or n%10 ==4:
    print (n, "программиста")
else:
    print (n,"программистов")

a = int(input())
while a <= 100:
    if a < 10:
        a = int(input())
        continue
    elif 10 <= a <= 100:
        print(a)

i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i = i + 1