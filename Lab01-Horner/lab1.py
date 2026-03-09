def horner(coffs,x):
    result = coffs[-1]
    for i in range (len(coffs) -2,-1, -1):
        result = result * x + coffs[i]
    return result

print("Progam do obliczania wielomianu metodą Hornera")
coffs_dane = input("Podaj współczynniki wielomianu w kolejności od najmniejszej potęgi do największej, odddzielając spacją:")
coffs = [float(c)for c in coffs_dane.split()]
x = float(input("Podaj x:"))

value = horner(coffs,x)
print(f"W({x}) = {value}")