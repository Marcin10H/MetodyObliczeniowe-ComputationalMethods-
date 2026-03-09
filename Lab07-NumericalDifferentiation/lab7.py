def oblicz_tablice_roznic_skonczonych(y):
    n = len(y)
    tabela = [[0.0] * n for _ in range(n)]
    for i in range(n):
        tabela[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            tabela[i][j] = tabela[i + 1][j - 1] - tabela[i][j - 1]
    return tabela

def pochodna_taylor_przod(tabela, h, n):
    wynik = 0.0
    for k in range(1, n):
        term = tabela[0][k]
        znak = 1.0 if k % 2 != 0 else -1.0
        wynik += znak * (1.0 / k) * term
    return wynik / h

def pochodna_taylor_wstecz(tabela, h, n):
    wynik = 0.0
    for k in range(1, n):
        wynik += (1.0 / k) * tabela[n - 1 - k][k]
    return wynik / h

def pochodna_stirling(tabela, h, idx):
    n = len(tabela)
    avg = (tabela[idx][1] + tabela[idx - 1][1]) / 2.0

    return avg / h

def roznice_dzielone(x, y):
    n = len(x)
    dd = [[0.0] * n for _ in range(n)]
    for i in range(n):
        dd[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            dd[i][j] = (dd[i + 1][j - 1] - dd[i][j - 1]) / (x[i + j] - x[i])
    return [dd[0][i] for i in range(n)]

def wypisz_wielomian(x, a):
    txt = f"W(x) = {a[0]:.4f}"
    for k in range(1, len(a)):
        znak = " + " if a[k] >= 0 else " - "
        skladnik = f"{abs(a[k]):.4f}"
        for i in range(k):
            skladnik += f"(x - {x[i]})"
        txt += znak + skladnik
    return txt

n = int(input("Podaj liczbę punktów n: "))
x = []
y = []
print("Wpisz x:")
for i in range(n): x.append(float(input(f"x[{i}] = ")))
print("Wpisz y:")
for i in range(n): y.append(float(input(f"y[{i}] = ")))

h = x[1] - x[0]
tab_roznic = oblicz_tablice_roznic_skonczonych(y)

while True:
    txt_in = input("Podaj x dla pochodnej (lub Enter aby wyjść): ")
    if not txt_in: break
    x_pt = float(txt_in)
    
    idx = -1
    for i in range(n):
        if abs(x[i] - x_pt) < 1e-9:
            idx = i
            break
            
    if idx == -1:
        print("Punkt musi być węzłem")
        continue
        
    if idx == 0:
        val = pochodna_taylor_przod(tab_roznic, h, n)
        metoda = "Taylor (Progresywna)"
    elif idx == n - 1:
        val = pochodna_taylor_wstecz(tab_roznic, h, n)
        metoda = "Taylor (Wsteczna)"
    else:
        val = pochodna_stirling(tab_roznic, h, idx)
        metoda = "Stirling (Centralna)"
        
    print(f"Metoda: {metoda}")
    print(f"f'({x_pt}) = {val:.5f}")

print("\nWielomian interpolacyjny Newtona:")
a_coeffs = roznice_dzielone(x, y)
print(wypisz_wielomian(x, a_coeffs))