def roznice_dzielone(xi, yi):
    n = len(xi)
    dd = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dd[i][0] = yi[i]

    for j in range(1, n):
        for i in range(n - j):
            dd[i][j] = (dd[i+1][j-1] - dd[i][j-1]) / (xi[i+j] - xi[i])
    a = [dd[0][j] for j in range(n)]
    return a, dd

def mnoz_wielomiany(p, q):
    wynik = [0.0] * (len(p) + len(q) - 1)

    for i in range(len(p)):
        for j in range(len(q)):
            wynik[i + j] += p[i] * q[j]
    return wynik

def dodaj_wielomiany(p, q):
    dl = max(len(p), len(q))
    p = p + [0.0] * (dl - len(p))
    q = q + [0.0] * (dl - len(q))
    return [p[i] + q[i] for i in range(dl)]

def wspolczynniki_newtona(xi, yi):
    a, dd = roznice_dzielone(xi, yi)
    n = len(xi)
    P = [0.0]

    for k in range(n):
        wiel = [1.0]
        for j in range(k):
            wiel = mnoz_wielomiany(wiel, [-xi[j], 1.0])
        wiel = [a[k] * c for c in wiel]

        if P == [0.0]:
            P = wiel
        else:
            P = dodaj_wielomiany(P, wiel)

    if len(P) < n:
        P = P + [0.0] * (n - len(P))
    return P, a, dd

def horner(coefs, x):
    wynik = 0.0
    for c in reversed(coefs):
        wynik = wynik * x + c
    return wynik

if __name__ == "__main__":

    print("Interpolacja Newtona")
    while True:
        try:
            n = int(input("Podaj liczbę punktów n (>=1)(pary liczb): "))

            if n >= 1:
                break
        except:
            pass
        print("Nieprawidłowa wartość. Spróbuj jeszcze raz.")

    xi = []
    yi = []

    print("Wpisz kolejne xi (liczby rzeczywiste):")

    for i in range(n):
        while True:
            try:
                v = float(input(f" xi[{i+1}] = "))
                xi.append(v)
                break
            except:
                print("Błędna liczba, spróbuj ponownie.")

    print("Wpisz odpowiadające wartości yi:")

    for i in range(n):
        while True:
            try:
                v = float(input(f" yi[{i+1}] = "))
                yi.append(v)
                break
            except:
                print("Błędna liczba, spróbuj ponownie.")

    wsp, a, dd = wspolczynniki_newtona(xi, yi)

    print("\nWspółczynniki Newtona a_k:")

    for idx, val in enumerate(a):
        print(f" a_{idx} = {val}")

    print("\nWspółczynniki wielomianu [a0 .. a{0}]:".format(len(wsp)-1))
    print(wsp)
    print("\nWeryfikacja P(xi) == yi:")

    for x, y in zip(xi, yi):
        val = horner(wsp, x)
        print(f"x = {x}, P(x) = {val}, y = {y}")
