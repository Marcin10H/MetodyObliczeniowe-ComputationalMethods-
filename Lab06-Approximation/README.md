# Lab 6: Approximation (Least Squares Method) | Aproksymacja (MNK) 📉

## Opis po polsku

Szóste laboratorium z przedmiotu **Metody Obliczeniowe** skupia się na metodzie najmniejszych kwadratów (MNK) oraz porównaniu jej charakterystyki z interpolacją wielomianową.

### 🚀 Zrealizowane zadania:

* **Obliczenia ręczne:** Wyznaczenie wzoru aproksymującej funkcji liniowej $Q_1(x) = a_0 + a_1x$ dla zbioru danych pomiarowych poprzez rozwiązanie układu równań normalnych.
* **Implementacja algorytmów:** Samodzielne stworzenie skryptów w językach **Python** i **MATLAB** (bez użycia gotowych bibliotek statystycznych) realizujących:
    * Aproksymację liniową MNK.
    * Interpolację Newtona (wykorzystując kod z poprzednich zajęć).
* **Wizualizacja i analiza:** Wykonanie wykresów porównawczych obu metod na jednym układzie współrzędnych w celu analizy różnic między dopasowaniem dokładnym (interpolacja) a przybliżonym (aproksymacja).

### 🧪 Wnioski

Interpolacja Newtona tworzy krzywą przechodzącą dokładnie przez wszystkie punkty, podczas gdy aproksymacja liniowa MNK wyznacza prostą najlepiej oddającą ogólny trend danych. W przypadku danych nieliniowych, aproksymacja uśrednia wyniki, co czyni ją bardziej stabilną przy analizie trendów.

### 📄 Dokumentacja

Pełny opis teoretyczny, obliczenia ręczne sum $S_k$ i $T_k$ oraz wykresy z obu środowisk znajdują się w załączonym sprawozdaniu: `MO_Lab06_Raport`.

---

## English Description

The sixth **Numerical Methods** laboratory focuses on the Least Squares Method (LSM) and comparing its characteristics with polynomial interpolation.

### 🚀 Tasks covered:

* **Manual Calculations:** Determining the formula for a linear approximating function $Q_1(x) = a_0 + a_1x$ for a given dataset by solving a system of normal equations.
* **Algorithm Implementation:** Custom development of **Python** and **MATLAB** scripts (without built-in statistical libraries) performing:
    * Linear LSM approximation.
    * Newton interpolation (reusing code from previous labs).
* **Visualization and Analysis:** Creating comparative plots for both methods on a single coordinate system to analyze the differences between exact fit (interpolation) and approximate fit (approximation).

### 🧪 Conclusions

Newton interpolation creates a curve that passes exactly through all data points, while linear LSM approximation determines a line that best represents the overall data trend. For non-linear data, approximation averages the results, making it more stable for trend analysis.

### 📄 Documentation

The full theoretical background, manual calculations of $S_k$ and $T_k$ sums, and plots from both environments are included in the attached PDF report: `MO_Lab06_Raport`.
