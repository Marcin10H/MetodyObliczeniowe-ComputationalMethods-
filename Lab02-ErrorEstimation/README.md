# Lab 2: Szacowanie błędów i Szeregi Maclaurina | Error Estimation & Maclaurin Series 📏

## Opis po polsku

Drugie laboratorium z przedmiotu **Metody Obliczeniowe** poświęcone jest analizie błędów pomiarowych oraz wykorzystaniu szeregów potęgowych (Maclaurina) do przybliżania wartości funkcji trygonometrycznych.

### 📋 Opis zadania

* **Analiza błędów:** Wykorzystanie metody różniczki zupełnej do obliczenia błędu bezwzględnego i względnego pola powierzchni brył (graniastosłup, walec).
* **Szeregi Maclaurina:** Implementacja algorytmu przybliżającego wartość funkcji `arcsin(x)` za pomocą sumy skończonej liczby wyrazów szeregu.
* **Porównanie środowisk:** Stworzenie skryptów w językach **Python** i **MATLAB** w celu zbadania, jak liczba wyrazów szeregu wpływa na błąd przybliżenia.

### 🧪 Wyniki

Na podstawie przeprowadzonych testów wykazano, że zwiększenie liczby wyrazów szeregu ($N$) znacząco redukuje błąd bezwzględny, przybliżając wynik do wartości dokładnej (funkcja biblioteczna `asin`).

### 📄 Dokumentacja

Pełny opis teoretyczny, wyprowadzenia wzorów na błędy oraz zrzuty ekranu z wynikami znajdują się w załączonym sprawozdaniu: `MO_Lab02_Raport.pdf`.

---

## English Description

The second **Numerical Methods** laboratory focuses on measuring error analysis and using power series (Maclaurin series) to approximate trigonometric function values.

### 📋 Task Description

* **Error Analysis:** Applying the total differential method to calculate absolute and relative errors of surface areas for various solids.
* **Maclaurin Series:** Implementation of an algorithm to approximate the `arcsin(x)` function using a sum of a finite number of series terms.
* **Software Comparison:** Developing scripts in **Python** and **MATLAB** to examine how the number of terms ($N$) affects the approximation error.

### 🧪 Results

Based on the tests conducted, it was demonstrated that increasing the number of series terms ($N$) significantly reduces the absolute error, bringing the result closer to the exact value (library function `asin`).

### 📄 Documentation

Full theoretical background, error formulas, and screenshots of the results are included in the attached PDF report: `MO_Lab02_Raport.pdf`.

