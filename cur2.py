n = int(input())
b = 0
if 1 <= n <= 100:
    while n > 0:
        m = int(input())
        n -= 1
        b += m
    print(b)
else:
    print(n, "неправильное число")

