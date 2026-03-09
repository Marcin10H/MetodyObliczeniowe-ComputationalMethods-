disp('Interpolacja Newtona');
n = input('Podaj liczbę punktów n (>=1): ');
while isempty(n) || n < 1
    n = input('Podaj poprawną liczbę punktów n (>=1): ');
end

xi = zeros(1, n);
yi = zeros(1, n);

disp('Wpisz kolejne xi:');
for i = 1:n
    xi(i) = input(sprintf(' xi(%d) = ', i));
end

disp('Wpisz odpowiadające yi:');
for i = 1:n
    yi(i) = input(sprintf(' yi(%d) = ', i));
end

[wsp, a, dd] = newton_conv(xi, yi);

disp('Wspolczynniki Newtona a_k:');
disp(a);

disp('Wspolczynniki wielomianu [a0..an]:');
disp(wsp);

disp('Weryfikacja P(xi) == yi:');
for i = 1:n
    wart = polyval(fliplr(wsp), xi(i));
    fprintf(' x = %.10g,  P(x)= %.10g,  y = %.10g\n', xi(i), wart, yi(i));
end

function [wspolczynniki, a, dd] = newton_conv(xi, yi)
    xi = xi(:).';
    yi = yi(:).';
    n = length(xi);
    dd = zeros(n,n);
    dd(:,1) = yi.';
    for j = 2:n
        for i = 1:(n-j+1)
            dd(i,j) = (dd(i+1,j-1) - dd(i,j-1)) / (xi(i+j-1) - xi(i));
        end
    end
    a = dd(1,:);
    P = [];
    for k = 0:(n-1)
        term = 1;
        for j = 1:k
            term = conv(term, [1, -xi(j)]);
        end
        if isempty(P)
            P = a(k+1) * term;
        else
            la = length(P);
            lb = length(term);
            if la < lb
                P = [zeros(1, lb-la), P];
            elseif lb < la
                term = [zeros(1, la-lb), term];
            end
            P = P + a(k+1) * term;
        end
    end
    wspolczynniki = fliplr(P);
end
