# Lab 9: Ordinary Differential Equations | Równania różniczkowe zwyczajne 📈

## Opis po polsku

Dziewiąte laboratorium z przedmiotu **Metody Obliczeniowe** poświęcone jest numerycznemu rozwiązywaniu równań różniczkowych zwyczajnych pierwszego rzędu z zadanym warunkiem początkowym (problem Cauchy'ego).

### 🚀 Zrealizowane zadania:

* **Analiza metod jednokrokowych:** Implementacja i porównanie dwóch algorytmów:
    * **Metoda Eulera:** Najprostsza metoda oparta na przybliżeniu styczną, charakteryzująca się dużą zależnością od kroku całkowania $h$.
    * **Metoda Rungego-Kutty IV rzędu (RK4):** Zaawansowany algorytm wykorzystujący cztery przybliżenia pochodnej w jednym kroku, co zapewnia znacznie większą stabilność i precyzję.
* **Obliczenia praktyczne:** Rozwiązanie równania $y' = -4.5xy + 3y - 2$ z warunkiem początkowym $y(0.5) = -1.0$.
* **Implementacja programistyczna:** Stworzenie samodzielnych skryptów w językach **Python** i **MATLAB** bez użycia wbudowanych solverów (takich jak `ode45`).

### 🧪 Wnioski

Metoda RK4 okazała się znacznie bardziej stabilna i płynna w porównaniu do metody Eulera, która przy tym samym kroku $h=0.1$ dawała mniej dokładne przybliżenie rzeczywistego przebiegu funkcji. Porównanie wyników w obu środowiskach potwierdziło poprawność zaimplementowanych algorytmów.

### 📄 Dokumentacja

Pełny opis teoretyczny, tabele wyników krok po kroku oraz kody źródłowe znajdują się w załączonym sprawozdaniu: `MO_Lab09_Raport.pdf`.

---

## English Description

The ninth **Numerical Methods** laboratory focuses on the numerical solution of first-order ordinary differential equations with a given initial condition (Cauchy problem).

### 🚀 Tasks covered:

* **One-step Methods Analysis:** Implementation and comparison of two algorithms:
    * **Euler's Method:** The simplest method based on tangent approximation, highly dependent on the integration step size $h$.
    * **4th Order Runge-Kutta Method (RK4):** An advanced algorithm utilizing four derivative approximations within a single step, ensuring much higher stability and precision.
* **Practical Calculations:** Solving the equation $y' = -4.5xy + 3y - 2$ with the initial condition $y(0.5) = -1.0$.
* **Software Implementation:** Developing standalone scripts in **Python** and **MATLAB** without utilizing built-in solvers (like `ode45`).

### 🧪 Conclusions

The RK4 method proved significantly more stable and smooth compared to Euler's method, which provided a less accurate approximation of the function's true behavior at the same step size $h=0.1$. Comparing results across both environments confirmed the correctness of the implemented algorithms.

### 📄 Documentation

The full theoretical background, step-by-step result tables, and source codes are included in the attached PDF report: `MO_Lab09_Raport.pdf`.
