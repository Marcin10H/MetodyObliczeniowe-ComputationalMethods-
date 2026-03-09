# Lab 7: Numerical Differentiation | Różniczkowanie numeryczne 📉

## Opis po polsku

Ostatnie laboratorium z przedmiotu **Metody Obliczeniowe** poświęcone jest technikom wyznaczania wartości pochodnej funkcji na podstawie dyskretnych zbiorów punktów pomiarowych.

### 🚀 Zrealizowane zadania:

* **Analiza teoretyczna:** Wykorzystanie wzorów różnicowych do obliczania pochodnej pierwszego rzędu:
    * **Metoda różnic wstecznych (wzór Taylora):** Stosowana dla punktów brzegowych przedziału.
    * **Metoda różnic centralnych (wzór Stirlinga):** Zapewniająca wyższą dokładność dla punktów wewnątrz przedziału.
* **Obliczenia ręczne:** Wyznaczenie wartości pochodnej w punktach $x=4.1$ (metoda Taylora) oraz $x=3.1$ (metoda Stirlinga) na podstawie tabeli różnic skończonych.
* **Implementacja algorytmów:** Stworzenie inteligentnych skryptów w językach **Python** i **MATLAB**, które automatycznie rozpoznają położenie punktu i dobierają optymalny wzór różnicowy (3- lub 5-punktowy).
* **Wielomian Newtona:** Wykorzystanie interpolacji jako metody pomocniczej do wyznaczania pochodnych.

### 🧪 Wnioski

Metoda różnic centralnych (Stirlinga) okazała się znacznie dokładniejsza, ponieważ analizuje wartości funkcji z obu stron badanego punktu. Wykazano, że dla uzyskania wyników zgodnych z teorią przy rzadkiej siatce węzłów, niezbędne jest uwzględnienie różnic wyższych rzędów.

### 📄 Dokumentacja

Pełny opis teoretyczny, tabele różnic skończonych oraz wyniki testów znajdują się w załączonym sprawozdaniu: `MO_Lab07_Raport`.

---

## English Description

The final **Numerical Methods** laboratory focuses on techniques for determining the derivative of a function based on discrete sets of data points.

### 🚀 Tasks covered:

* **Theoretical Analysis:** Using finite difference formulas to calculate the first-order derivative:
    * **Backward Difference Method (Taylor formula):** Used for boundary points of the interval.
    * **Central Difference Method (Stirling formula):** Providing higher accuracy for points inside the interval.
* **Manual Calculations:** Determining derivative values at points $x=4.1$ (Taylor method) and $x=3.1$ (Stirling method) based on the finite difference table.
* **Algorithm Implementation:** Developing intelligent scripts in **Python** and **MATLAB** that automatically detect the point's position and select the optimal difference formula (3- or 5-point).
* **Newton Polynomial:** Using interpolation as a supporting tool for determining derivatives.

### 🧪 Conclusions

The central difference method (Stirling) proved to be significantly more accurate as it analyzes function values on both sides of the point. It was demonstrated that higher-order differences are essential to maintain theoretical accuracy when data points are sparse.

### 📄 Documentation

The full theoretical background, finite difference tables, and test results are included in the attached PDF report: `MO_Lab07_Raport`.
