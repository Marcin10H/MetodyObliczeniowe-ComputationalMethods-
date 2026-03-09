def mnk_linear(x, y):
    n = len(x)
    S0 = n
    S1 = 0.0
    S2 = 0.0
    T0 = 0.0
    T1 = 0.0

    for i in range(n):
        S1 += x[i]
        S2 += x[i] * x[i]
        T0 += y[i]
        T1 += x[i] * y[i]

    det = S0 * S2 - S1 * S1
    a0 = (T0 * S2 - S1 * T1) / det
    a1 = (S0 * T1 - S1 * T0) / det
    return a0, a1

def roznice_dzielone(xi, yi):
    n = len(xi)
    dd = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dd[i][0] = yi[i]

    for j in range(1, n):
        for i in range(n - j):
            dd[i][j] = (dd[i+1][j-1] - dd[i][j-1]) / (xi[i+j] - xi[i])
    a = [dd[0][j] for j in range(n)]
    return a

def newton_eval(a, x_nodes, x):

    n = len(a)
    result = a[-1]

    for k in range(n - 2, -1, -1):
        result = result * (x - x_nodes[k]) + a[k]
    return result

def wypisz_wielomian_newtona(a, x):
    n = len(a)
    wynik = f"P(x) = {a[0]}"
    for k in range(1, n):
        wynik += f" + {a[k]}"
        for j in range(k):
            wynik += f"(x - {x[j]})"
    return wynik

print("Interpolacja Newtona + Aproksymacja MNK")

while True:
    try:
        n = int(input("Podaj liczbę punktów n (>=1): "))
        if n >= 1:
            break
    except:
        pass
    print("Błędna wartość.")

x = []
y = []

print("\nWpisz wartości xi:")

for i in range(n):
    while True:
        try:
            v = float(input(f" xi[{i+1}] = "))
            x.append(v)
            break
        except:
            print("Błąd. Spróbuj ponownie.")

print("\nWpisz wartości yi:")

for i in range(n):
    while True:
        try:
            v = float(input(f" yi[{i+1}] = "))
            y.append(v)
            break
        except:
            print("Błąd. Spróbuj ponownie.")

print("\nAPROKSYMACJA LINIOWA MNK")
a0, a1 = mnk_linear(x, y)
print(f"a0 = {a0}")
print(f"a1 = {a1}")
print(f"f(x) = {a0} + {a1} * x")

print("\nINTERPOLACJA NEWTONA")

a_newton = roznice_dzielone(x, y)

print("Współczynniki Newtona a_k:")

for i, val in enumerate(a_newton):
    print(f"a[{i}] = {val}")

print("\nWielomian interpolacyjny (postać Newtona):")
print(wypisz_wielomian_newtona(a_newton, x))

print("\nWeryfikacja P(xi) == yi:")
for xi, yi_val in zip(x, y):
    print(f"x = {xi}, P(x) = {newton_eval(a_newton, x, xi)}, y = {yi_val}")
