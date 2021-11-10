#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 11:07:47 2021

@author: arne
"""

import numpy as np
import matplotlib.pyplot as plt


Drehzahl = np.array([600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600])
DynamischerDruck = np.array([20,25,30,39,46,57,68,80,94,108,124])
Windgeschwindigkeit = np.sqrt(2*DynamischerDruck/1.2)
Rücktriebk = np.array([0,0,0.03,0.04,0.05,0.07,0.09,0.1,0.13,0.15,0.18])
Rücktriebg = np.array([0.025,0.05,0.08,0.115,0.15,0.22,0.26,0.32,0.38,0.45,0.51])

plt.xlabel('Windgeschwindigkeit (m/s)')
plt.ylabel('Rücktrieb (N)')
plt.plot(Windgeschwindigkeit, Rücktriebk)
plt.plot(Windgeschwindigkeit, Rücktriebg)
plt.legend(['kleine Kreisscheibe (r=2cm)', 'große Kreisscheibe (r=4cm)'])
plt.show()
plt.xlabel('Dynamischer Druck (pascal)')
plt.ylabel('Rücktrieb (N)')
plt.plot(DynamischerDruck, Rücktriebk)
plt.plot(DynamischerDruck, Rücktriebg)
plt.legend(['kleine Kreisscheibe (r=2cm)', 'große Kreisscheibe (r=4cm)'])
plt.show()