import matplotlib.pyplot as plt#fazer graficos

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
qTI = [60 , 52, 76, 89, 108, 95]
qRH = [40 , 72, 17, 28, 87, 56]

# plt.plot(meses,qTI,label ="TI",color="green",linestyle ="--",marker = ".")
# plt.plot(meses,qRH, label = 'RH',color="blue",linestyle ="-",marker = "o")
# plt.title("Chamados abertos")
# plt.xlabel("Meses")
# plt.ylabel("Quantidade")
# plt.legend()
# # plt.show()

navegadores = ["Chrome"," Firefox", "Edge"]
qtd = [1200, 600, 200]
cores = ["red","orange", "blue"]
plt.pie(qtd,labels=navegadores,colors=cores)
plt.show()