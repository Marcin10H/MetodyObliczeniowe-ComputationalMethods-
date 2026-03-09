function lab9matlab()
    disp('LABORATORIUM: Rownania Rozniczkowe Zwyczajne')
    while true
        disp('1. Zadanie 1 (Euler + RK4)');
        disp('2. Zadanie 4 / Przyklad 19 (RK4)');
        disp('3. Wyjscie');
        wybor = input('Twoj wybor: ', 's');
        if strcmp(wybor, '1')
            f = @(x, y) -4.5 * x * y + 3 * y - 2;
            x0 = 0.5; xk = 1.0; y0 = -1.0; h = 0.1;
            euler_method(f, x0, y0, xk, h);
            rk4_method(f, x0, y0, xk, h);
        elseif strcmp(wybor, '2')
            f = @(x, y) (x^2) + y + (y/x);
            x0 = 1.0; xk = 2.0; y0 = 0.6; h = 0.1;
            rk4_method(f, x0, y0, xk, h);
        elseif strcmp(wybor, '3')
            break
        end
    end
end

function euler_method(f, x0, y0, xend, h)
    disp('Wyniki metoda EULERA:');
    fprintf('%-5s %-10s %-15s\n', 'Iter', 'x', 'y');
    x = x0; y = y0; iter = 0;
    fprintf('%-5d %-10.4f %-15.6f\n', iter, x, y);
    while x < xend - 1e-9
        iter = iter + 1;
        y = y + h * f(x, y);
        x = x + h;
        fprintf('%-5d %-10.4f %-15.6f\n', iter, x, y);
    end
end

function rk4_method(f, x0, y0, xend, h)
    disp('Wyniki metoda RK4:');
    fprintf('%-5s %-10s %-15s\n', 'Iter', 'x', 'y');
    x = x0; y = y0; iter = 0;
    fprintf('%-5d %-10.4f %-15.6f\n', iter, x, y);
    while x < xend - 1e-9
        iter = iter + 1;
        k1 = h * f(x, y);
        k2 = h * f(x + 0.5*h, y + 0.5*k1);
        k3 = h * f(x + 0.5*h, y + 0.5*k2);
        k4 = h * f(x + h, y + k3);
        y = y + (k1 + 2*k2 + 2*k3 + k4) / 6.0;
        x = x + h;
        fprintf('%-5d %-10.4f %-15.6f\n', iter, x, y);
    end
end