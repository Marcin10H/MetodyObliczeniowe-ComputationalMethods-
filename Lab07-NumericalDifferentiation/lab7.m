function lab7matlab()
    clc;
    n = input('Podaj liczbe punktow n: ');
    xi = zeros(1,n);
    yi = zeros(1,n);

    disp('Wpisz x:');
    for i=1:n
        xi(i) = input(sprintf('x(%d) = ', i));
    end
    disp('Wpisz y:');
    for i=1:n
        yi(i) = input(sprintf('y(%d) = ', i));
    end

    h = xi(2) - xi(1);
    D = zeros(n, n);
    D(:,1) = yi';
    for j=2:n
        for i=1:(n-j+1)
            D(i,j) = D(i+1,j-1) - D(i,j-1);
        end
    end

    x_pt = input('Podaj x dla pochodnej: ');
    if ~isempty(x_pt)
        idx = find(abs(xi - x_pt) < 1e-9);
        if isempty(idx)
            disp('Punkt musi byc wezlem.');
        else
            if idx == 1
                der = taylor_przod(D, h, n);
                met = 'Taylor (Progresywna)';
            elseif idx == n
                der = taylor_tyl(D, h, n);
                met = 'Taylor (Wsteczna)';
            else
                der = stirling(D, h, idx, n);
                met = 'Stirling (Centralna)';
            end
            fprintf('Metoda: %s\n', met);
            fprintf('f''(%g) = %.5f\n', x_pt, der);
        end
    end

    dd = zeros(n,n);
    dd(:,1) = yi(:);
    for j=2:n
        for i=1:(n-j+1)
            dd(i,j) = (dd(i+1,j-1) - dd(i,j-1)) / (xi(i+j-1) - xi(i));
        end
    end
    a = dd(1,:);
    fprintf('\nW(x) = %.4f', a(1));
    for k=2:n
        if a(k) >= 0, s = '+'; else, s = '-'; end
        fprintf(' %s %.4f', s, abs(a(k)));
        for j=1:(k-1)
            fprintf('(x-%.4g)', xi(j));
        end
    end
    fprintf('\n');
end

function res = taylor_przod(D, h, n)
    res = 0;
    for k=1:(n-1)
        res = res + ((-1)^(k-1)) * (1/k) * D(1, k+1);
    end
    res = res / h;
end

function res = taylor_tyl(D, h, n)
    res = 0;
    for k=1:(n-1)
        res = res + (1/k) * D(n-k, k+1);
    end
    res = res / h;
end

function res = stirling(D, h, idx, n)
    avg = (D(idx, 2) + D(idx-1, 2)) / 2;
    res = avg / h;
end