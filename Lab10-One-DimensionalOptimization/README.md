# Lab 10: One-Dimensional Optimization | Optymalizacja jednowymiarowa 🎯

## Opis po polsku

Dziesiąte laboratorium z przedmiotu **Metody Obliczeniowe** dotyczy wyznaczania ekstremum (minimum) funkcji jednej zmiennej w zadanym przedziale $[a, b]$. Głównym narzędziem wykorzystanym w zadaniach jest metoda złotego podziału.

### 🚀 Zrealizowane zadania:

* **Analiza teoretyczna:** Porównanie metod bezgradientowych: dychotomii, Fibonacciego oraz złotego podziału.
* **Obliczenia ręczne:** Wyznaczenie minimum funkcji $f(x) = x^3 + 0.5x^2 - 4x - 1$ w przedziale $[0.5, 5.0]$ przy użyciu trzech kroków metody dychotomii.
* **Implementacja algorytmów:** Stworzenie skryptów w językach **Python** i **MATLAB** realizujących metodę złotego podziału. Programy pozwalają na interaktywny wybór funkcji celu oraz parametrów optymalizacji (przedział, dokładność $\epsilon$).
* **Wizualizacja:** Generowanie wykresów w MATLAB-ie prezentujących przebieg funkcji oraz precyzyjne wskazanie znalezionego punktu minimum.

### 🧪 Wnioski

Metoda złotego podziału wykazała się wysoką efektywnością numeryczną dzięki ponownemu wykorzystaniu punktów wewnętrznych w kolejnych iteracjach. Pozwala to na znaczną redukcję liczby wywołań funkcji celu przy zachowaniu stabilnej zbieżności do wyniku.

### 📄 Dokumentacja

Pełny opis teoretyczny, tabele przebiegu iteracji oraz wykresy znajdują się w załączonym sprawozdaniu: `MO_Lab10_Raport.pdf`.

---

## 🇬🇧 English Description

The tenth **Numerical Methods** laboratory focuses on determining the extremum (minimum) of a single-variable function within a given interval $[a, b]$. The primary tool used for these tasks is the Golden Section Search method.

### 🚀 Tasks covered:

* **Theoretical Analysis:** Comparing derivative-free optimization methods: Dichotomy (Bisection), Fibonacci, and Golden Section Search.
* **Manual Calculations:** Finding the minimum of the function $f(x) = x^3 + 0.5x^2 - 4x - 1$ in the interval $[0.5, 5.0]$ using three steps of the dichotomy method.
* **Algorithm Implementation:** Developing scripts in **Python** and **MATLAB** that implement the Golden Section Search. The programs allow for interactive selection of the objective function and optimization parameters (interval, tolerance $\epsilon$).
* **Visualization:** Generating plots in MATLAB to present the function's behavior and precisely highlight the calculated minimum point.

### 🧪 Conclusions

The Golden Section Search method demonstrated high numerical efficiency by reusing internal points in subsequent iterations. This allows for a significant reduction in the number of objective function calls while maintaining stable convergence to the result.

### 📄 Documentation

The full theoretical background, iteration tables, and plots are included in the attached PDF report: `MO_Lab10_Raport.pdf`.
