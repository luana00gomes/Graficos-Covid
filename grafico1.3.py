#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 20:15:45 2020

@author: Luana Gomes e Widmark Cardoso

Gráfico1.3: As linhas partem do ponto para os eixos cordenados simutaneamente  
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time


plt.style.use('dark_background') #seta estilo para escuro


#Espaços vazios para variação dos lines
x1_data = []
y1_data = []

x2_data = []
y2_data = []


#Cria o objeto figura com os eixos cordenados e suas delimitações.
fig1, ax1 = plt.subplots()
ax1.set_xlim(0, 13)
ax1.set_ylim(0,40)

#Cria as linhas que receberão as funções e seta ponto inicial nos eixos gerados
line1, = ax1.plot(10, 32,'--')
line2, = ax1.plot(10, 32,'--')


#Determina o comportamento da função
def animation_frame1(i):
    x2_data.append(10)
    y2_data.append(32-i)
    line2.set_xdata(x2_data)
    line2.set_ydata(y2_data)
        
    x1_data.append(10-i*0.3125) #0.315 = 10/32 - fator de correção
    y1_data.append(32)
        
    line1.set_xdata(x1_data)
    line1.set_ydata(y1_data)
        
    return line1, line2


#Determina o comportamento da função
def animation_frame2(i):
    x2_data.append(10)
    y2_data.append(4-i)
    
    line2.set_xdata(x2_data)
    line2.set_ydata(y2_data)
    return line2,


"""
*
tempo_execucao= num_max_frames / taxa_atualizacao_frames

Útil para definir tempo da animação e realizar sincronização. 
-------------------------------------------------------------
Objeto animation: Recebe uma função que tem como principais parâmetros de entrada uma figura criada
anteriormente, o comportamento da função criada, um vetor indicando os frames e a taxa de atualização 
e a condição de repetição.

**
Para adequar o tempo de execução numa mesma animation é necessário utilizar um fator de
correção nas funções que determinam o comportamento da line.
Desse modo, multiplicando i por pelo resultado de x/y na line que corre paralela em x 
ou y/x, na line que corre paralela a y é possível ajustar o tempo de execução de ambas
as lines.

"""


#Função f1: Linha paralela ao eixo x
animation1 = FuncAnimation(fig1, func=animation_frame1, frames=np.arange(0, 33, 1), interval=1,repeat = False)


#Função f2: Linha paralela ao eixo y
# animation2 = FuncAnimation(fig1, func=animation_frame2, frames=np.arange(0, 4, 0.016), interval=1, repeat = False)

#Função base: Background da animação
x=np.linspace(0,12,1000)
y=2**(x/2)
plt.plot(x, y)

plt.plot(10,32,'o', label = "N(10) = 32")
plt.ylabel('Casos')
plt.xlabel('Dias')
plt.legend()

plt.show()

# animation1.save('grafico1.3.gif',writer='imagemagick') 
