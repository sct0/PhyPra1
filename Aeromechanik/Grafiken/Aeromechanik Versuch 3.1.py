#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 22:02:48 2021

@author: arne
"""

import numpy as np
import matplotlib.pyplot as plt

Anstellwinkel = np.array([-20,-15,-10,-5,0,5,10,15,20])
Auftrieb = np.array([-0.3,-0.2,0,0,0.1,0.1,0.3,0.4,0.55])
Rücktrieb = np.array([0.15,0.1,0.06,0.07,0.09,0.1,0.12,0.17,0.29])

plt.xlabel('Anstellwinkel (Grad)')
plt.ylabel('Auftrieb (N)')
plt.plot(Anstellwinkel,Auftrieb,'r')
plt.show()

plt.xlabel('Anstellwinkel (Grad)')
plt.ylabel('Rücktrieb (N)')
plt.plot(Anstellwinkel,Rücktrieb,'r')
plt.show()

plt.xlabel('Rücktrieb (N)')
plt.ylabel('Auftrieb (N)')
plt.plot(Rücktrieb, Auftrieb, 'or')
x = np.linspace(0,0.3,100)
y = (Auftrieb[6]/Rücktrieb[6])*x
y1 = (Auftrieb[7]/Rücktrieb[7])*x
y2 = (Auftrieb[8]/Rücktrieb[8])*x
plt.plot(x,y)
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()