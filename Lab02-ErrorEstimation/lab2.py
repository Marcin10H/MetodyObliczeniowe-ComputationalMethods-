from math import asin

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    

def szereg(x,liczbaOkresow):
    wynik = 0
    for n in range(liczbaOkresow):
        licznik = factorial(2*n)
        mianownik = (4**n)*(factorial(n)**2)*(2*n+1)
        skladnik = (licznik/mianownik)*(x**(2*n+1))
        wynik += skladnik
    return wynik


print("Obliczenie arcsin(x) przy użyciu Szeregu Maclaurina")
x = float(input("Podaj wartosc x:"))
liczbaOkresow = int(input("Podaj liczbe wyrazow szeregu:"))

wartoscPrzyblizona = szereg(x,liczbaOkresow)
wartoscDokladna = asin(x)
blad = abs(wartoscPrzyblizona-wartoscDokladna)

print(f"arcsin(x) przyblizony(N = {liczbaOkresow}):{wartoscPrzyblizona:.10f}")
print(f"arcsin(x) dokladny(asin): {wartoscDokladna:.10f}")
print(f"Blad bezwzgledny: {blad:.2e}")
