s=input().lower().split()
d={i : s.count(i) for i in s}
for key,value in d.items():
    print(key,value)