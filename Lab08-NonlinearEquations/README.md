# Lab 8: Nonlinear Equations | Równania nieliniowe 🔍

## Opis po polsku

Ósme laboratorium z przedmiotu **Metody Obliczeniowe** skupia się na numerycznym wyznaczaniu miejsc zerowych funkcji jednej zmiennej. W ramach zajęć przeanalizowano efektywność i szybkość zbieżności różnych algorytmów iteracyjnych.

### 🚀 Zrealizowane zadania:

* **Analiza metod numerycznych:** Implementacja trzech podstawowych algorytmów:
    **Metoda bisekcji:** Stabilna i niezawodna, choć wymagająca większej liczby iteracji.
    **Metoda cięciw:** Wykorzystująca liniową aproksymację funkcji.
    **Metoda stycznych (Newtona):** Najszybsza pod względem zbieżności, wykorzystująca pochodną numeryczną funkcji.
**Automatyzacja:** Stworzenie skryptu automatycznie wyszukującego przedział, w którym funkcja zmienia znak (warunek konieczny dla metody bisekcji).
**Obliczenia ręczne:** Wyznaczenie pierwiastka równania $2x^3+2x^2+4x=3$ w przedziale [0.4, 0.6] przy zadanej dokładności $\epsilon=0.1$.

### 🧪 Wnioski

Metoda bisekcji okazała się najbardziej stabilna dla złożonych funkcji, podczas gdy metoda stycznych oferowała najszybsze znalezienie rozwiązania przy poprawnym doborze punktu początkowego. Wybór metody powinien być zawsze dostosowany do charakteru funkcji oraz jej dziedziny.

### 📄 Dokumentacja

Pełny opis teoretyczny, tabele iteracji oraz kody źródłowe znajdują się w załączonym sprawozdaniu: `MO_Lab08_Raport`.

---

## English Description

The eighth **Numerical Methods** laboratory focuses on the numerical determination of roots (zeros) for functions of a single variable. The course analyzed the efficiency and convergence speed of various iterative algorithms.

### 🚀 Tasks covered:

* **Numerical Methods Analysis:** Implementation of three core algorithms:
    **Bisection Method:** Stable and reliable, though requiring more iterations.
    **Secant Method:** Utilizing linear approximation of the function.
    **Newton's Method (Tangent Method):** Fastest in terms of convergence, utilizing the numerical derivative of the function.
**Automation:** Developing a script to automatically search for an interval where the function changes sign (a prerequisite for the bisection method).
**Manual Calculations:** Finding the root of the equation $2x^3+2x^2+4x=3$ in the interval [0.4, 0.6] with a specified tolerance $\epsilon=0.1$.

### 🧪 Conclusions

The bisection method proved most stable for complex functions, while Newton's method offered the fastest solution given a correctly chosen starting point. The choice of a numerical method should always be tailored to the function's characteristics and its domain.

### 📄 Documentation

The full theoretical background, iteration tables, and source codes are included in the attached PDF report: `MO_Lab08_Raport`.
