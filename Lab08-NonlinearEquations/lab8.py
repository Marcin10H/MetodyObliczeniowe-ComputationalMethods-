import math

def funkcja_zad1(x):
    return 2*(x**3) + 2*(x**2) + 4*x - 3

def funkcja_zad4(x):
    if x <= 0:
        return -1000.0
    return math.log10(x) - (7 / (2*x + 6))

def szukaj_przedzialu(f, start, krok=0.5, limit=100):
    print(f"Szukam przedziału (start={start}, krok={krok})...")
    a = start
    for _ in range(limit):
        b = a + krok
        if f(a) * f(b) < 0:
            print(f"Znaleziono przedział: [{a:.2f}, {b:.2f}]")
            return a, b
        a = b
    print("Nie udało się znaleźć przedziału w zadanym limicie kroków.")
    return None, None

def metoda_bisekcji(f, a, b, epsilon):
    print(f"METODA BISEKCJI (przedział [{a:.4f}, {b:.4f}])")
    if f(a) * f(b) > 0:
        print("Błąd: Funkcja nie zmienia znaku na końcach przedziału")
        return None
    
    print(f"{'Iter':<5} {'a':<10} {'b':<10} {'x_srodek':<10} {'f(x)':<10}")
    iteracja = 0
    while True:
        iteracja += 1
        x_srodek = (a + b) / 2
        f_srodek = f(x_srodek)
        print(f"{iteracja:<5} {a:<10.5f} {b:<10.5f} {x_srodek:<10.5f} {f_srodek:<10.6f}")
        
        if abs(f_srodek) < epsilon:
            return x_srodek
        
        if f(a) * f_srodek < 0:
            b = x_srodek
        else:
            a = x_srodek

def metoda_cieciw(f, a, b, epsilon):
    print("METODA CIĘCIW")
    x1, x2 = a, b
    iteracja = 0
    print(f"{'Iter':<5} {'x_k':<10} {'f(x)':<10}")
    while True:
        iteracja += 1
        fx1, fx2 = f(x1), f(x2)
        if abs(fx2 - fx1) < 1e-9: break
        x_nowy = x2 - fx2 * (x2 - x1) / (fx2 - fx1)
        print(f"{iteracja:<5} {x_nowy:<10.5f} {f(x_nowy):<10.6f}")
        if abs(f(x_nowy)) < epsilon:
            return x_nowy
        x1, x2 = x2, x_nowy

def metoda_stycznych(f, start, epsilon):
    print("METODA STYCZNYCH")
    x = start
    iteracja = 0
    h = 1e-5
    print(f"{'Iter':<5} {'x':<10} {'f(x)':<10}")
    while abs(f(x)) > epsilon:
        iteracja += 1
        dfx = (f(x + h) - f(x)) / h
        x = x - f(x) / dfx
        print(f"{iteracja:<5} {x:<10.5f} {f(x):<10.6f}")
    return x

while True:
    print("\n1. Zadanie 1 (2x^3...) - wpisujesz przedział")
    print("2. Zadanie 4 / Przykład 19 (log10...) - PROGRAM SZUKA PRZEDZIAŁU")
    print("3. Wyjście")
    wybor = input("Twój wybór: ")
    
    if wybor == '1':
        eps = float(input("Podaj epsilon (np. 0.1): "))
        a = float(input("Podaj a przedziału (np. 0.4): "))
        b = float(input("Podaj b przedziału (np. 0.6): "))
        metoda_bisekcji(funkcja_zad1, a, b, eps)
        metoda_cieciw(funkcja_zad1, a, b, eps)
        metoda_stycznych(funkcja_zad1, b, eps)
    elif wybor == '2':
        eps = float(input("Podaj epsilon: "))
        a_auto, b_auto = szukaj_przedzialu(funkcja_zad4, 0.1, 0.5)
        if a_auto is not None:
            wynik = metoda_bisekcji(funkcja_zad4, a_auto, b_auto, eps)
            print(f"Wynik dla Przykładu 19: x = {wynik:.5f}")
    elif wybor == '3':
        break