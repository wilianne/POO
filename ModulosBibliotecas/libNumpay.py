import numpy as np#fazer calculos mais rapidos

numeros = [10 ,2 ,3 ,4 ,5, 7, 9, 10]

soma = 0

for n in numeros:
    soma += n
    
media = soma/len(numeros)
print(f"media na mao: {media}")

array_numeros = np.array(numeros)

media = np.mean(array_numeros)
print(f"media com o numpay: {media}")
