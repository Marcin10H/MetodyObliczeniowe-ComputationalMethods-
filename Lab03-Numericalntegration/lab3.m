clc; clear;

f = @(x) 3*x.^5 + 2*x.^4 - 4*x.^3 + 3*x.^2 - 5*x + 2;
a = 1;
b = 7;

disp('WYZNACZANIE WARTOŚCI CAŁKI METODĄ TRAPEZÓW');
fprintf('Funkcja: f(x) = %s\n', func2str(f));
fprintf('Przedział: [%g, %g]\n', a, b);

n = input('Podaj liczbę przedziałów n (np. 10, 20, 50): ');

if isempty(n) || n <= 0 || floor(n) ~= n
    error('n musi być dodatnią liczbą całkowitą.');
end

h = (b - a) / n;
x = a:h:b;
y = f(x);
S = h * (0.5*y(1) + sum(y(2:end-1)) + 0.5*y(end));

fprintf('\nDla n = %d\n', n);
fprintf('Wartość całki ? %.10f\n', S);
