function lab8matlab()
    clc;
    disp('LABORATORIUM 8: Rownania Nieliniowe');
    while true
        disp('1. Zadanie 1');
        disp('2. Zadanie 4 / Przyklad 19');
        disp('3. Wyjscie');
        wybor = input('Wybierz: ');
        
        if wybor == 1
            f = @(x) 2*x.^3 + 2*x.^2 + 4*x - 3;
            eps = input('Epsilon (np. 0.1): ');
            a = input('a: '); b = input('b: ');
            bisekcja(f, a, b, eps);
            cieciwa(f, a, b, eps);
            newton(f, b, eps);
        elseif wybor == 2
            f = @(x) log10(x) - (7./(2*x + 6));
            eps = input('Epsilon (np. 0.01): ');
            [a_zn, b_zn] = szukaj_przedzialu(f, 0.1, 0.5);
            if ~isnan(a_zn)
                wynik = bisekcja(f, a_zn, b_zn, eps);
                fprintf('\n>>> Ostateczny wynik: x = %.5f\n', wynik);
            else
                disp('Nie udalo sie znalezc przedzialu.');
            end
        elseif wybor == 3
            break;
        end
    end
end

function [a, b] = szukaj_przedzialu(f, start, krok)
    fprintf('Szukam przedzialu (start=%.1f)...\n', start);
    x = start; limit = 100;
    for i = 1:limit
        fa = f(x); fb = f(x + krok);
        if fa * fb < 0
            a = x; b = x + krok;
            fprintf('- Znaleziono przedzial: [%.2f, %.2f]\n', a, b);
            return;
        end
        x = x + krok;
    end
    a = NaN; b = NaN;
end

function wynik = bisekcja(f, a, b, eps)
    fprintf('\nMetoda Bisekcji\n');
    iter = 0; x = (a + b) / 2;
    fprintf('Iter | a | b | x_sr | f(x)\n');
    while abs(f(x)) > eps
        iter = iter + 1; x = (a + b) / 2;
        fprintf('%4d | %.5f | %.5f | %.5f | %.5f\n', iter, a, b, x, f(x));
        if f(a) * f(x) < 0
            b = x;
        else
            a = x;
        end
    end
    wynik = x;
end

function wynik = cieciwa(f, a, b, eps)
    fprintf('\nMetoda Cieciw\n');
    x1 = a; x2 = b; iter = 0;
    while true
        iter = iter + 1;
        fx1 = f(x1); fx2 = f(x2);
        x_nowy = x2 - fx2 * (x2 - x1) / (fx2 - fx1);
        fprintf('Iter %d: x = %.5f\n', iter, x_nowy);
        if abs(f(x_nowy)) < eps, break; end
        x1 = x2; x2 = x_nowy;
    end
    wynik = x_nowy;
end

function wynik = newton(f, x_start, eps)
    fprintf('\nMetoda Stycznych\n');
    x = x_start; iter = 0; h = 1e-5;
    while abs(f(x)) > eps
        iter = iter + 1;
        dfx = (f(x + h) - f(x)) / h;
        x = x - f(x) / dfx;
        fprintf('Iter %d: x = %.5f\n', iter, x);
    end
    wynik = x;
end