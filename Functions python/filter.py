numeros = [1,2,3,4,5,6,7,8,9,10]


resultado = filter(lambda n: n % 2 == 1 , numeros)
print(list(resultado))