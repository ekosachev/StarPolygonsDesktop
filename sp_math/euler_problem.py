from math import pi, cos

from draw_sp import oriented_area

def fibonacci_series(n):
    series = []
    a, b = 0, 1

    while len(series) < n:
        series.append(a)
        a, b = b, a + b

    return series

fib = fibonacci_series(36)

areas = []
for i in range(3, 35):
    n = fib[i+1]
    m = fib[i-1]
    areas.append(oriented_area(n, m, (1 / cos(pi * m / n))))

print(round(sum(areas), 10))