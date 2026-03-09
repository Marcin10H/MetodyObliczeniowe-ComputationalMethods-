import math

def funkcja_zad1(x):
    return x**3 + 0.5 * x**2 - 4 * x - 1

def funkcja_zad19(x):
    # Przykład 19: 0.25*x^2 - sin(x)
    return 0.25 * x**2 - math.sin(x)

def zloty_podzial(f, a, b, epsilon):
    k = (math.sqrt(5) - 1) / 2
    x1 = b - k * (b - a)
    x2 = a + k * (b - a)
    iteracja = 0
    
    print(f"\n{'Iteracja':<10} {'a':<10} {'b':<10} {'x1':<10} {'x2':<10} {'f(x1)':<10} {'f(x2)':<10}")
    
    while abs(b - a) > epsilon:
        iteracja += 1
        fx1 = f(x1)
        fx2 = f(x2)
        print(f"{iteracja:<10} {a:<10.4f} {b:<10.4f} {x1:<10.4f} {x2:<10.4f} {fx1:<10.4f} {fx2:<10.4f}")
        
        if fx1 < fx2:
            b = x2
            x2 = x1
            x1 = b - k * (b - a)
        else:
            a = x1
            x1 = x2
            x2 = a + k * (b - a)
            
    return (a + b) / 2

print("Wybierz zadanie do rozwiązania:")
print("1. Zadanie 1: f(x) = x^3 + 0.5x^2 - 4x - 1")
print("2. Zadanie 4 (Przykład 19): f(x) = 0.25x^2 - sin(x)")
wybor = input("Twój wybór: ")

if wybor == '1':
    f_celu = funkcja_zad1
    a_in, b_in = 0.5, 5.0
    eps = 0.01
elif wybor == '2':
    f_celu = funkcja_zad19
    a_in, b_in = 0.0, 2.0 # Przykładowy przedział
    eps = 0.001
else:
    print("Niepoprawny wybór.")
    exit()

wynik = zloty_podzial(f_celu, a_in, b_in, eps)
print(f"\nZnalezione minimum (x*): {wynik:.5f}")
print(f"Wartość funkcji w minimum f(x*): {f_celu(wynik):.5f}")