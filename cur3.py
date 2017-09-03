def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return (5 - x % 5) + x


x = int(input())
y = closest_mod_5(x)
print(y)
