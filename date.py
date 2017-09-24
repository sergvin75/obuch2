import datetime

n, m, k = (int(i) for i in input().split())
w = int(input())
x = datetime.date(n,m,k)
datetime.timedelta = w

print(x)
print(datetime.timedelta)