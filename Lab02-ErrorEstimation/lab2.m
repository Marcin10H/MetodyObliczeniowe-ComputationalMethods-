function szereg()
    disp('Obliczanie arcsin(x) za pomoc¹ szeregu Maclaurina');
    x = input('Podaj wartoœæ x: ');
    liczbaOkresow = input('Podaj liczbê wyrazów szeregu: ');
    
    wynik = 0;

    for n = 0:(liczbaOkresow - 1)
        licznik = factorial(2 * n);
        mianownik = (4^n) * (factorial(n)^2) * (2 * n + 1);
        skladnik = (licznik / mianownik) * (x^(2 * n + 1));
        wynik = wynik + skladnik;
    end

    disp(['arcsin(x) przybli¿ony (N = ', num2str(liczbaOkresow), '): ', num2str(wynik)]);

    % Sprawdzenie

    wartoscDokladna = asin(x);
    blad = abs(wynik - wartoscDokladna);
    disp(['arcsin(x) dok³adny (asin): ', num2str(wartoscDokladna)]);
    disp(['B³¹d bezwzglêdny: ', num2str(blad)]);
end

