n=int(input())
if 1 <= n <= 100:
    while a <= 100:
    m = int(input())
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
