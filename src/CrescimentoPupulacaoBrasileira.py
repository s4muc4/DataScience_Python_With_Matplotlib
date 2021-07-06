#Crescimento da População Brasileira 1980-2016

import matplotlib.pyplot as plt

dados = open("populacao_brasileira.csv").readlines();

x = []
y = []

for i in range(len(dados)):
	if i != 0:
		linha = dados[i].split(";")
		x.append(int(linha[0]))
		y.append(int(linha[1]))

plt.title("Crescimento da População Brasileira 1980-2016")		
plt.xlabel("Ano")
plt.ylabel("População x100 milhões")

plt.bar(x, y)
plt.plot(x, y, label = "crescimento", linestyle = "--", color = "k")
#plt.show()
plt.savefig("CrescimentoPopulacional.png", dpi = 300)