numeros = [10,20,30,17,58,3,7]

print(numeros[5])

carros = ['Palio','Gol','Virtus','Ka','Onix']
print(carros)

carros.append("Kombi")
print(carros)

carros.remove("Gol")
print(carros)

carros = sorted(carros)
print(carros)

for i in range(len(carros)):
    print(carros[i])

for carro in carros:
    print(carro)