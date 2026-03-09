# Lab 4: Systems of Linear Equations | Układy równań liniowych 🔢

## Opis po polsku

Czwarte laboratorium z przedmiotu **Metody Obliczeniowe** poświęcone jest rozwiązywaniu układów równań liniowych. Głównym celem była implementacja i analiza metody eliminacji Gaussa.

### 🚀 Zrealizowane zadania:

* **Obliczenia ręczne:** Rozwiązanie układu 3 równań z 3 niewiadomymi przy użyciu:
    * Metody eliminacji Gaussa (sprowadzanie macierzy do postaci trójkątnej).
    * Metody Cramera (wykorzystanie wyznaczników macierzy).
* **Implementacja algorytmów:** Stworzenie własnych funkcji w językach **Python** (z użyciem `numpy`) oraz **MATLAB** realizujących pełny proces eliminacji Gaussa z podstawianiem wstecznym.
* **Weryfikacja poprawności:** Sprawdzenie warunku $A \cdot x \approx b$ w celu potwierdzenia dokładności uzyskanych wyników.

### 🧪 Wnioski

Metoda eliminacji Gaussa okazała się znacznie efektywniejsza dla większych układów niż metoda Cramera. Implementacja w obu środowiskach (Python i MATLAB) dała identyczne, poprawne rezultaty.

### 📄 Dokumentacja

Pełny opis teoretyczny, obliczenia ręczne oraz zrzuty ekranu z wynikami znajdują się w załączonym sprawozdaniu: `MO_Lab04_Raport.pdf`.

---

## English Description

The fourth **Numerical Methods** laboratory focuses on solving systems of linear equations. The primary objective was the implementation and analysis of the Gaussian elimination method.

### 🚀 Tasks covered:

* **Manual Calculations:** Solving a system of 3 equations with 3 unknowns using:
    * Gaussian elimination (reducing the matrix to upper triangular form).
    * Cramer's rule (using matrix determinants).
* **Algorithm Implementation:** Developing custom functions in **Python** (using `numpy`) and **MATLAB** to perform full Gaussian elimination with back-substitution.
* **Verification:** Checking the $A \cdot x \approx b$ condition to confirm the accuracy of the results.

### 🧪 Conclusions

The Gaussian elimination method proved to be significantly more efficient for larger systems compared to Cramer's rule. Implementations in both environments (Python and MATLAB) yielded identical, correct results.

### 📄 Documentation

The full theoretical background, manual calculations, and result screenshots are included in the attached PDF report: `MO_Lab04_Raport.pdf`.
