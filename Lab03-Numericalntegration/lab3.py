import math
import inspect


#Przykład 19

def f(x):
    return 3*x**5 + 2*x**4 - 4*x**3 + 3*x**2 - 5*x + 2

def metodaTrapezow(f, a, b, n):
    h = (b - a) / n
    s = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        s += f(a + i*h)
    return s * h

a = 1
b = 7

print("WYZNACZANIE CAŁKI METODĄ TRAPEZÓW")

source = inspect.getsource(f).strip()
func_body = source.split("return")[-1].strip()

print(f"Funkcja: f(x) = {func_body}")
print(f"Przedział: [{a}, {b}]")

try:
    n = int(input("Podaj liczbę przedziałów n (np. 10, 20, 50): "))
    if n <= 0:
        raise ValueError
except ValueError:

    print("Błąd: n musi być dodatnią liczbą całkowitą.")
    exit()

wynik = metodaTrapezow(f, a, b, n)

print(f"\nDla n = {n}")
print(f"Wartość całki ≈ {wynik:.10f}")

