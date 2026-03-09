function eliminacja_gaussa()

    clc;
    disp('Rozwi¹zywanie uk³adu równañ liniowych metod¹ Gaussa');

    n = input('Podaj liczbê równañ w uk³adzie(n): ');

    macierz_A = zeros(n, n);
    wektor_b = zeros(n, 1);

    fprintf('\nPodaj wspó³czynniki macierzy A:\n');

    for i = 1:n
        for j = 1:n
            prompt = sprintf('A(%d,%d) = ', i, j);
            macierz_A(i,j) = input(prompt);
        end
    end

    fprintf('\nPodaj wyrazy wolne (wektor b):\n');
    
    for i = 1:n
        prompt = sprintf('b(%d) = ', i);
        wektor_b(i) = input(prompt);
    end

    rozwiazanie = gauss_rozwiaz(macierz_A, wektor_b);

    fprintf('\nRozwi¹zanie uk³adu równañ metod¹ Gaussa:\n');

    for i = 1:n
        fprintf('x%d = %.4f\n', i, rozwiazanie(i));
    end

    % Sprawdzenie

    disp(' ');
    disp('Sprawdzenie: macierz_A * rozwiazanie = ');
    disp(macierz_A * rozwiazanie);
    disp('Oczekiwane b = ');
    disp(wektor_b);
end


function rozwiazanie = gauss_rozwiaz(macierz_A, wektor_b)
    macierz_A = double(macierz_A);
    wektor_b = double(wektor_b);
    n = length(wektor_b);

    for i = 1:n
        if macierz_A(i,i) == 0
            for j = i+1:n
                if macierz_A(j,i) ~= 0               

                    tempA = macierz_A(i,:);
                    macierz_A(i,:) = macierz_A(j,:);
                    macierz_A(j,:) = tempA;

                    tempb = wektor_b(i);
                    wektor_b(i) = wektor_b(j);
                    wektor_b(j) = tempb;
                    break;
                end
            end
        end

        for j = i+1:n
            wsp = macierz_A(j,i) / macierz_A(i,i);
            macierz_A(j,i:n) = macierz_A(j,i:n) - wsp * macierz_A(i,i:n);
            wektor_b(j) = wektor_b(j) - wsp * wektor_b(i);
        end
    end

    rozwiazanie = zeros(n,1);

    for i = n:-1:1
        rozwiazanie(i) = (wektor_b(i) - macierz_A(i,i+1:n) * rozwiazanie(i+1:n)) / macierz_A(i,i);
    end
end