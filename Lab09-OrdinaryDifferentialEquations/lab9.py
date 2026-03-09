import math

def funkcja_zad1(x, y):
    return -4.5 * x * y + 3 * y - 2

def funkcja_zad19(x, y):
    if x == 0:
        return 0
    return (x**2) + y + (y / x)

def metoda_eulera(f, x0, y0, x_koniec, h):
    print("\nMETODA EULERA")
    print(f"{'Iter': <5} {'x':<10} {'y':<15}")
    x = x0
    y = y0
    iteracja = 0
    print(f"{iteracja: <5} {x:<10.4f} {y:<15.6f}")
    while x < x_koniec - 1e-9:
        iteracja += 1
        y = y + h * f(x, y)
        x = x + h
        print(f"{iteracja: <5} {x:<10.4f} {y:<15.6f}")

def metoda_rk4(f, x0, y0, x_koniec, h):
    print("\nMETODA RUNGEGO-KUTTY 4 (RK4)")
    print(f"{'Iter': <5} {'x':<10} {'y':<15}")
    x = x0
    y = y0
    iteracja = 0
    print(f"{iteracja: <5} {x:<10.4f} {y:<15.6f}")
    while x < x_koniec - 1e-9:
        iteracja += 1
        k1 = h * f(x, y)
        k2 = h * f(x + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(x + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(x + h, y + k3)
        delta_y = (k1 + 2 * k2 + 2 * k3 + k4) / 6.0
        y = y + delta_y
        x = x + h
        print(f"{iteracja: <5} {x:<10.4f} {y:<15.6f}")

while True:
    print("\nLAB: Równania Różniczkowe Zwyczajne")
    print("1. Zadanie 1 (Test: Euler + RK4)")
    print("2. Zadanie 4 / Przykład 19")
    print("3. Wyjście")
    wybor = input("Twój wybór: ")
    if wybor == '1':
        print("\nDANE TESTOWE (Zadanie 1)")
        x_start = 0.5
        x_stop = 1.0
        y_start = -1.0
        h = 0.1
        metoda_eulera(funkcja_zad1, x_start, y_start, x_stop, h)
        metoda_rk4(funkcja_zad1, x_start, y_start, x_stop, h)
    elif wybor == '2':
        print("\nPRZYKŁAD 19 (Zadanie 4)")
        x_start = 1.0
        x_stop = 2.0
        y_start = 0.6
        h = 0.1
        metoda_rk4(funkcja_zad19, x_start, y_start, x_stop, h)
    elif wybor == '3':
        break