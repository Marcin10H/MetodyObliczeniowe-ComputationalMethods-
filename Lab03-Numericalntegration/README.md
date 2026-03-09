# Lab 3: Numerical Integration | Całkowanie numeryczne 📐

## Opis po polsku

Trzecie laboratorium z przedmiotu **Metody Obliczeniowe** poświęcone jest numerycznemu wyznaczaniu wartości całek oznaczonych. Metody te są niezbędne, gdy rozwiązanie analityczne jest zbyt trudne do uzyskania lub funkcja jest zdefiniowana dyskretnie.

### 🚀 Zrealizowane zadania:

* **Obliczenia ręczne:** Wyznaczenie wartości całki z wielomianu 5. stopnia na przedziale [1, 7] przy użyciu czterech metod:
    * Metoda prostokątów (z niedomiarem i nadmiarem).
    * Metoda trapezów.
    * Metoda Simpsona (parabol).
* **Implementacja algorytmów:** Stworzenie skryptów w językach **Python** i **MATLAB** realizujących metodę trapezów.
* **Analiza zbieżności:** Badanie wpływu liczby podprzedziałów ($n$) na dokładność wyniku (testowane dla $n$ od 10 do 500).

### 🧪 Wnioski

Zwiększenie liczby przedziałów ($n$) prowadzi do wyraźnej poprawy dokładności i zbieżności wyniku do wartości dokładnej. Metoda trapezów okazała się efektywnym kompromisem między prostotą implementacji a precyzją.

### 📄 Dokumentacja

Pełny opis teoretyczny, obliczenia ręczne (schemat Hornera) oraz zrzuty ekranu z wynikami znajdują się w załączonym sprawozdaniu: `MO_Lab03_Raport.pdf`.

---

## English Description

The third **Numerical Methods** laboratory focuses on the numerical determination of definite integral values. These methods are essential when an analytical solution is too difficult to obtain or when the function is defined discretely.

### 🚀 Tasks covered:

* **Manual Calculations:** Evaluating the integral of a 5th-degree polynomial over the interval [1, 7] using four methods:
    * Rectangle method (left-hand and right-hand sums).
    * Trapezoidal rule.
    * Simpson's rule (parabolic approximation).
* **Algorithm Implementation:** Developing **Python** and **MATLAB** scripts for the trapezoidal rule.
* **Convergence Analysis:** Examining the impact of the number of sub-intervals ($n$) on result accuracy (tested for $n$ values from 10 to 500).

### 🧪 Conclusions

Increasing the number of intervals ($n$) leads to a clear improvement in accuracy and convergence toward the exact value. The trapezoidal rule proved to be an effective compromise between implementation simplicity and precision.

### 📄 Documentation

The full theoretical background, manual calculations (Horner's scheme), and result screenshots are included in the attached PDF report: `MO_Lab03_Raport.pdf`.
