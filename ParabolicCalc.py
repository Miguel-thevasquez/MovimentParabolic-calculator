# -*- coding: utf-8 -*-
"""
Created on Thu Jan  5 08:17:13 2023
Always comment all the program, 
@author: Miguel Angel
"""

# libraries
import numpy as np
import matplotlib.pyplot as plt

# constants (Time and Gravity)
T = 0
G = 9.8
# inputs (angle and initial velocity)
Ang = 0
Iv = 0
# ascention time (At) and Flying Time (Flt)
#At = Iv * sin(Ang) / G
#Flt = 2 * At
#
# distance axis X and Y
# for X
# X = Iv + Cos(Ang) * T
# Time increses from 1 to maximum Flt

# for Y
#(Iv * Sin(Ang)*T) - (0.5 * G * T**2)
# time increses depending on Flt

# velocities X(Vx) and Y(Vy) and Vp (Velocity proyectile)
# for X Iv * cos(Ang)
# for Y Iv * sin(Ang)
# for proyectile sqrt(vx**2 + vy**2)


class Parabole_ecu:

    def ATFT(x, y, z):  # Ascension Time and Flying time // x for Iv, Y for Ang and z for T

        At = x * np.sin(np.radians(y)) / z
        Flt = 2*At
        return At, Flt

    def Distance(a, b, c, d):  # a for Iv, b for Ang, c for time and d for G

        X = a * np.cos(np.radians(b)) * c
        Y = (a * np.sin(np.radians(b)) * c) - (0.5 * d * np.power(c, 2))
        if Y < 0:
            Y *= -1
        return X, Y

    def Speed(a, b):    # a for Iv and b for Ang
        Vx = a * np.cos(b)
        Vy = a * np.sin(b)
        Vp = np.sqrt(np.power(Vx, 2) + np.power(Vy, 2))
        return Vx, Vy, Vp


Xs = []
Ys = []
Iv, Ang = float(input("set a initial velocity on m/s\n")
                ), float(input("set an angle on degrees\n"))

At, flt = Parabole_ecu.ATFT(Iv, Ang, G)
while T <= flt+1:

    if T < flt:
        X, Y = Parabole_ecu.Distance(Iv, Ang, T, G)
        Xs.append(X)
        Ys.append(Y)
        T += 0.1

    elif T >= flt:
        vx, vy, vp = Parabole_ecu.Speed(Iv, Ang)
        print(" the maximum distance traveled is: {}m \n".format(str(round(max(Xs), 1))),
              "the maximum altitude is: {}m\n".format(str(round(max(Ys), 1))),
              "the maximum velocity of the proyectile is: {}m/s \n".format(str(vp)))
        break

plt.plot(Xs, Ys, "--")
