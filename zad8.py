a = int(input())
while a <= 100:
    if a < 10:
        a = int(input())
        continue
    elif 10 <= a <= 100:
        print(a)
        a = int(input())