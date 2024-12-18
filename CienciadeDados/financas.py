import pandas as pd
import matplotlib.pyplot as plt

class Investimentos:
    def __init__(self, nome, valor, taxa, periodo):
        self.nome = nome
        self.valor = valor
        self.taxa = taxa
        self.periodo = periodo
        

investimentos = {
    "Investimento 1": Investimentos('Tesouro Direto',10000,0.002,5),
    "Investimento 2": Investimentos('Acoes',435,0.2,4),
    "Investimento 3": Investimentos('Poupanca',8000,0.01,10),
    "Investimento 4": Investimentos('CBD',15000,0.03,7)
}
lista_de_investimentos = [i.__dict__ for i in investimentos.values()]
df_investimento = pd.DataFrame.from_records(lista_de_investimentos,index=investimentos.keys())

df_investimento['retorno'] = df_investimento.apply(lambda l: l.valor * (1 + l.taxa)** l.periodo,axis=1)

df_investimento.plot(kind='pie',y='retorno',legend='nome')
plt.title('Retorno dos Investimentos')
plt.xlabel('Investimentos')
plt.ylabel('Retorno em reais')
plt.show()
