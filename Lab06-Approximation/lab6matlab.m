disp("Interpolacja Newtona + Aproksymacja MNK");

n = input("Podaj liczbę punktów n (>=1): ");
while isempty(n) || n < 1
    n = input("Podaj poprawną liczbę punktów n (>=1): ");
end

xi = zeros(1,n);
yi = zeros(1,n);

disp("Wpisz kolejne xi:");
for i = 1:n
    xi(i) = input(sprintf(" xi(%d) = ", i));
end

disp("Wpisz kolejne yi:");
for i = 1:n
    yi(i) = input(sprintf(" yi(%d) = ", i));
end

[a0, a1] = mnk_linear(xi, yi);

fprintf("\nAPROKSYMACJA LINIOWA MNK\n");
fprintf("a0 = %f\n", a0);
fprintf("a1 = %f\n", a1);
fprintf("f(x) = %f + %f * x\n", a0, a1);

a = roznice_dzielone(xi, yi);

disp("INTERPOLACJA NEWTONA");
disp("Współczynniki Newtona:");
disp(a);
disp("Wielomian interpolacyjny (postać Newtona):");
disp( wypisz_wielomian_newtona(a, xi) );

disp("Weryfikacja:");
for i = 1:n
    val = newton_eval(a, xi, xi(i));
    fprintf("x = %.10f, P(x)= %.10f, y = %.10f\n", xi(i), val, yi(i));
end

function [a0, a1] = mnk_linear(x, y)
n = length(x);
S0 = n;
S1 = sum(x);
S2 = sum(x.^2);
T0 = sum(y);
T1 = sum(x .* y);

detA = S0 * S2 - S1 * S1;
a0 = (T0 * S2 - S1 * T1) / detA;
a1 = (S0 * T1 - S1 * T0) / detA;
end

function a = roznice_dzielone(xi, yi)
n = length(xi);
dd = zeros(n,n);
dd(:,1) = yi(:);

for j = 2:n
    for i = 1:(n-j+1)
        dd(i,j) = (dd(i+1,j-1) - dd(i,j-1)) / (xi(i+j-1) - xi(i));
    end
end

a = dd(1,:);
end

function val = newton_eval(a, x_nodes, x)
n = length(a);
val = a(n);
for k = n-1:-1:1
    val = val * (x - x_nodes(k)) + a(k);
end
end

function txt = wypisz_wielomian_newtona(a, x)
    n = length(a);
    txt = sprintf("P(x) = %.10g", a(1));

    for k = 2:n
        txt = txt + sprintf(" + %.10g", a(k));
        for j = 1:(k-1)
            txt = txt + sprintf("(x - %.10g)", x(j));
        end
    end
end
