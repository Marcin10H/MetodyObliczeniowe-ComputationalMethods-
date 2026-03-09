import numpy as np


def eliminacja_gaussa(macierz_A, wektor_b):
    macierz_A = macierz_A.astype(float)
    wektor_b = wektor_b.astype(float)
    n = len(wektor_b)

    for i in range(n):
        if macierz_A[i, i] == 0:
            for j in range(i + 1, n):
                if macierz_A[j, i] != 0:
                    macierz_A[[i, j]] = macierz_A[[j, i]]
                    wektor_b[[i, j]] = wektor_b[[j, i]]
                    break

        for j in range(i + 1, n):
            wspolczynnik = macierz_A[j, i] / macierz_A[i, i]
            macierz_A[j, i:] -= wspolczynnik * macierz_A[i, i:]
            wektor_b[j] -= wspolczynnik * wektor_b[i]

    rozwiazanie = np.zeros(n)

    for i in range(n - 1, -1, -1):
        rozwiazanie[i] = (wektor_b[i] - np.dot(macierz_A[i, i + 1:], rozwiazanie[i + 1:])) / macierz_A[i, i]
    return rozwiazanie


print("--- Rozwiązywanie układu równań liniowych metodą eliminacji Gaussa ---")

n = int(input("Podaj liczbę równań (n): "))
macierz_A = np.zeros((n, n))
wektor_b = np.zeros(n)

print("\nWprowadź współczynniki macierzy A:")

for i in range(n):
    for j in range(n):
        macierz_A[i, j] = float(input(f"A[{i+1},{j+1}] = "))


print("\nWprowadź wyrazy wolne (wektor b):")

for i in range(n):
    wektor_b[i] = float(input(f"b[{i+1}] = "))


rozwiazanie = eliminacja_gaussa(macierz_A, wektor_b)

print("\nRozwiązanie układu:")

for i in range(n):
    print(f"x{i+1} = {rozwiazanie[i]:.4f}")

# Sprawdzenie

print("\nSprawdzenie poprawności (A·x):")
print(np.dot(macierz_A, rozwiazanie))
print("Oczekiwane b:")
print(wektor_b)