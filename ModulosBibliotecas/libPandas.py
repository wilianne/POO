import pandas as pd #fazer tabelas

cidades = [
    {"nome":"Sao Paulo","uf":"SP","populacao":1000000000000},
    {"nome":"Rio de Janeiro","uf":"RJ","populacao":123454636},
    {"nome":"Distrito Federal","uf":"DF","populacao":5677685856},
    {"nome":"Recife","uf":"PE","populacao":78923898521}
]

dataframe = pd.DataFrame(cidades)

ordenada = dataframe.sort_values(by='populacao',ascending=False)
print(ordenada)
print(ordenada.head(2)['nome'])