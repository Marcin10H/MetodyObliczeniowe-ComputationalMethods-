function lab10matlab()
    clc;
    disp('Wybór zadania');
    disp('1. Zadanie 1: f(x)=x^3+0.5x^2-4x-1');
    disp('2. Zadanie 4 (Przykład 19): f(x)=0.25x^2-sin(x)');
    wybor = input('Wybierz numer: ');

    if wybor == 1
        f = @(x) x.^3 + 0.5*x.^2 - 4*x - 1;
        a = 0.5; b = 5; eps = 0.01;
    elseif wybor == 2
        f = @(x) 0.25*x.^2 - sin(x);
        a = 0; b = 2; eps = 0.001;
    else
        error('Nieprawidłowy wybór');
    end

    k = (sqrt(5) - 1) / 2;
    x1 = b - k * (b - a);
    x2 = a + k * (b - a);
    iter = 0;

    fprintf('\nWyniki metody Złotego Podziału:\n');
    fprintf('%10s %10s %10s %10s %10s\n', 'Iter', 'a', 'b', 'x1', 'x2');

    while abs(b - a) > eps
        iter = iter + 1;
        fx1 = f(x1); fx2 = f(x2);
        fprintf('%10d %10.4f %10.4f %10.4f %10.4f\n', iter, a, b, x1, x2);
        
        if fx1 < fx2
            b = x2; x2 = x1;
            x1 = b - k * (b - a);
        else
            a = x1; x1 = x2;
            x2 = a + k * (b - a);
        end
    end

    x_min = (a + b) / 2;
    fprintf('\nZnalezione minimum x* = %.5f\n', x_min);
    fprintf('Wartość funkcji f(x*) = %.5f\n', f(x_min));

    % Wykres [cite: 6141]
    fplot(f, [a-1, b+1], 'LineWidth', 1.5); hold on;
    plot(x_min, f(x_min), 'ro', 'MarkerSize', 10, 'MarkerFaceColor', 'r');
    grid on; title('Wykres funkcji i znalezione minimum');
end