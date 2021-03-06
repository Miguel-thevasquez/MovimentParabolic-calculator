# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 16:30:48 2020
-----simulador parabola---------------------------
@author: Miguel-thevasquez

"""
import math
import matplotlib.pyplot as plt

#start
print("bienvenido al simulador de trayectoria ")
print("Created by Miguel Ángel Vásquez Quintero")
print("Github: Miguel-thevasquez")
print("ingrese angulo de lanzamiento y velocidad inicial")
print("--tiene un margen de error de 0.01% --")
print("use estandar internacional")

#variables fijas-------------------------------------------------
t = 0
g = 9.8
#variables entrada-----------------------------------------------
print("ingrese angulo de inclinación")
gr = math.radians(int(input()))
print("ingrese velocidad de lanzamiento")
vo = float(input())
# time-----------------------------------------------------------

ts = vo * math.sin(gr) / g
tv = 2*ts
#distance--------------------------------------------------------

x = vo * math.cos(gr) * t 
xt = []
xi = 0

y = (vo * math.sin(gr) * t) - (0.5 * g * t**2)
yt = []
yi = int(0)
#velocity--------------------------------------------------------

vx = float(vo * math.cos(gr))
vy = float(vo * math.sin(gr) - g * t)
vp = float(math.sqrt(vx**2 + vy**2))
#program---------------------------------------------------------
while t <= tv:
    if tv > 1:
        x = vo * math.cos(gr) * t 
        y = (vo * math.sin(gr) * t) - (0.5 * g * t**2)
        t = t+0.1
        xt.append(x)
        yt.append(y)
    elif t <= 1:
        x = vo * math.cos(gr) * t 
        y = (vo * math.sin(gr) * t) - (0.5 * g * t**2)
        t = t+0.0001
        xt.append(x)
        yt.append(y)
    
plt.plot(xt, yt, color = "green", linewidth = 2, label = "lineal")
plt.legend()
plt.show()
xi = len(xt)-1
yi = len(yt)/2
print("altura maxima",float(yt[int(yi)]),"m") #y maximo
print("distancia maxima",float(xt[int(xi)]),"m") # x maximo
print("velocidad Horizontal",vx,"m/s")
print("velocidad vertical",vy,"m/s")
print("velocidad del proyectil",vp,"m/s")










