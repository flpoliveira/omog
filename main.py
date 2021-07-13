from scipy.interpolate import BSpline
import matplotlib.pyplot
import numpy as np
import math

# B-spline não uniforme de grau 3
m = 3
k = 3
knots =  [0,1,2,5,6,8,10] #m+k+1 #randomicamente
Pi = [[0,0],[1,1],[2,0],[3,3]] #usado no trab: Pi = [[0,0],[1,1],[2,0],[3,3]]
p0 = [Pi[0][0], Pi[1][0], Pi[2][0], Pi[3][0]] #Usando para plotar os pontos lá em baixo
p1 = [Pi[0][1], Pi[1][1], Pi[2][1], Pi[3][1]] #Usando para plotar os pontos lá em baixo

def bspline(t):
    retorno = [0,0]
    for i in range(0,m+1):
        retorno[0] = retorno[0] + (Pi[i][0] * bsplineBasis(i,k,t))
        retorno[1] = retorno[1] + (Pi[i][1] * bsplineBasis(i,k,t))
    return (retorno)

def bsplineBasis(i,k,t):
    if k==1:
        if knots[i] <= t and t < knots[i+1]:
            return 1
        else:
            return 0
    else:
        return (((t-knots[i])/(knots[i+k-1] - knots[i])) * bsplineBasis(i, k-1,t)) + (((knots[i+k] - t)/(knots[i+k] - knots[i+1])) * bsplineBasis(i+1, k-1, t))
  

#Agora vamos fazer a minha curva B-spline não uniforme de grau 3
t1 = knots[2]
saidinha_bspline = []
x_bspline = []
y_bspline = []

while t1 < knots[5]:
    saidinha_bspline.append(bspline(t1))
    t1 = t1 + 0.1
    
for xaca in saidinha_bspline:
    x_bspline.append(xaca[0])
    y_bspline.append(xaca[1])
#Agora eu tenho as listas x_spline e y_spline com os valores a serem plotados

matplotlib.pyplot.plot(x_bspline, y_bspline)

matplotlib.pyplot.plot(p0, p1, 'o')
matplotlib.pyplot.show()