n=int(input())
if (n//10)%10 == 1:
    print (n,"программистов")
elif n%10 == 1:
    print (n," программист")
elif n%10 == 2 or n%10 ==3 or n%10 ==4:
    print (n, "программиста")
else:
    print (n,"программистов")
