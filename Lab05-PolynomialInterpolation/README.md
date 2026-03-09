# Lab 5: Polynomial Interpolation | Interpolacja wielomianowa 📈

## Opis po polsku

Piąte laboratorium z przedmiotu **Metody Obliczeniowe** poświęcone jest technikom przybliżania funkcji na podstawie ograniczonego zbioru punktów pomiarowych. Głównym celem była implementacja interpolacji w postaci Newtona oraz Lagrange'a.

### 🚀 Zrealizowane zadania:

* **Obliczenia ręczne:** Wyznaczenie funkcji interpolacyjnej $y=f(x)$ dla zadanego zbioru 4 punktów przy użyciu:
    * Wielomianu Newtona opartego na różnicach dzielonych.
    * Wielomianu Lagrange'a.
* **Implementacja algorytmów:** Stworzenie skryptów w językach **Python** i **MATLAB**. Wersja pythonowa została napisana bez użycia zewnętrznych bibliotek, co wymagało zaimplementowania własnych funkcji do mnożenia i dodawania wielomianów.
* **Weryfikacja:** Sprawdzenie, czy otrzymany wielomian przechodzi dokładnie przez wszystkie punkty wejściowe (warunek $W(x_i) = y_i$).

### 🧪 Wnioski

Implementacja w Pythonie pozwoliła na dogłębne zrozumienie struktury wielomianu Newtona, podczas gdy MATLAB umożliwił szybszą realizację zadania dzięki wbudowanym funkcjom operującym na wielomianach (np. `conv`). W obu przypadkach uzyskano wyniki o wysokiej precyzji, zgodne z danymi wejściowymi.

### 📄 Dokumentacja

Pełny opis teoretyczny, tabele różnic dzielonych oraz zrzuty ekranu z wynikami znajdują się w załączonym sprawozdaniu: `MO_Lab05_Raport`.

---

## English Description

The fifth **Numerical Methods** laboratory focuses on techniques for approximating functions based on a limited set of data points. The primary objective was the implementation of Newton and Lagrange interpolation forms.

### 🚀 Tasks covered:

* **Manual Calculations:** Determining the interpolation function $y=f(x)$ for a given set of 4 points using:
    * Newton's divided difference interpolation.
    * Lagrange's interpolating polynomial.
* **Algorithm Implementation:** Developing scripts in **Python** and **MATLAB**. The Python version was developed from scratch without external libraries, requiring custom functions for polynomial addition and multiplication.
* **Verification:** Confirming that the resulting polynomial passes exactly through all input data points (the $W(x_i) = y_i$ condition).

### 🧪 Conclusions

The Python implementation provided a deep understanding of the Newton polynomial structure, while MATLAB allowed for faster development using built-in polynomial functions (e.g., `conv`). Both environments yielded high-precision results consistent with the input data.

### 📄 Documentation

The full theoretical background, divided difference tables, and result screenshots are included in the attached PDF report: `MO_Lab05_Raport`.
