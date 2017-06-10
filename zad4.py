text = input()
if text == 'треугольник':
    a, b, c = float(input()), float(input()), float(input())
    p = (a + b + c) / 2
    print((p * (p - a) * (p - b) * (p - c)) ** 0.5)
elif text == 'прямоугольник':
    a, b = float(input()), float(input())
    print(a * b)
elif text == 'круг':
    r = float(input())
    print(3.14 * (r ** 2))