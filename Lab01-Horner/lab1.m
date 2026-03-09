disp('Progam do obliczania wielomianu metod¹ Hornera');
coffs_dane = input('Podaj wspó³czynniki wielomianu w kolejnoœci od najmniejszej potêgi do najwiêkszej, odddzielaj¹c spacj¹:','s');
coffs = str2num(coffs_dane);
%#ok<ST2NM>
x=input('Podaj x:');

n=length(coffs);
value=coffs(end);
for i=n-1:-1:1
    value=value*x+coffs(i);
end

fprintf('W(%g)=%g\n',x,value);