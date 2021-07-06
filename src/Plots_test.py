#Visualização de dados em Python


""" 
#CORES - color
'b' as blue
'g' as green
'r' as red
'c' as cyan
'm' as magenta
'y' as yellow
'k' as black
'w' as white 

OBS: Pode usar Hexadecimal para cor também

#MARCADORES - marker
'.' point marker
',' pixel marker
'o' circle marker
'v' triangle_down marker
'^' triangle_up marker
'<' triangle_left marker
'>' triangle_right marker
'1' tri_down marker
'2' tri_up marker
'3' tri_left marker
'4' tri_right marker
's' square marker
'p' pentagon marker
'*' star marker
'h' hexagon1 marker
'H' hexagon2 marker
'+' plus marker
'x' x marker
'D' diamond marker
'd' thin_diamond marker
'|' vline marker
'_' hline marker

#TIPOS DE LINHA - linestyle
'-' solid line style
'--' dashed line style
'-.' dash-dot line style
':' dotted line style
"""

import matplotlib.pyplot as plt

x1 = [1, 3, 5, 7, 9]
y1 = [2, 3, 7, 1, 3]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 1, 3, 7, 4]

titulo = "Scatterplot: gráfico de dispersão"
eixoX = "Eixo X"
eixoY = "Eixo Y"
grupo1 = "Grupo 1"
grupo2 = "Grupo 2"


#Legendas
plt.title(titulo)
plt.xlabel(eixoX)
plt.ylabel(eixoY)

#CRIA GRÁFICO DE LINHA
#plt.plot(x, y) 

#CRIA GRÁFICO DE BARRAS COM LEGENDAS
#plt.bar(x1, y1, label = grupo1)
#plt.bar(x2, y2, label = grupo2)
#EXIBE LABEL
#plt.legend()   



plt.scatter(x1, y1, label = "Meus pontos", color = "k", marker = ".", s = 200)
plt.plot(x1,y1, color = "k", linestyle = "-.")
plt.legend()

#Mostra Gráfico
#plt.show()

#Salva Gráfico
#plt.savefig("figura1.pdf")
plt.savefig("figura1.png", dpi=300)