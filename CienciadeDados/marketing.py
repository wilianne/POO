import matplotlib.pyplot as plt

class Campanha:
    def __init__(self, canal, investimento, cliques, conversoes):
       self.canal = canal
       self.investimento = investimento
       self.cliques = cliques
       self.conversoes = conversoes
       
    def custo_por_clique(self):
        return self.investimento / self.cliques
    

campanhas = [
    Campanha('Facebook Ads', 1000, 15000,150),
    Campanha('Google Ads', 1200, 10000,200),
    Campanha('Email Ads', 500, 5000,50),
    Campanha('Instagram Ads', 800, 12000,80),
]

canais = [c.canal for c in campanhas]
cpc = [c.custo_por_clique() for c in campanhas]


plt.bar(canais,cpc)
plt.title("Custo por cliques")
plt.xlabel("Canais")
plt.ylabel("Custo em R$")
plt.show()