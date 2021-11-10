#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 18:37:18 2021

@author: arne
"""

import numpy as np
import matplotlib.pyplot as plt


Drehzahl = np.array([600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600])
DynamischerDruck = np.array([20,25,30,39,46,57,68,80,94,108,124])
Windgeschwindigkeit = np.sqrt(2*DynamischerDruck/1.2)
print(Windgeschwindigkeit)


plt.xlabel('Drehzahl (rpm)')
plt.ylabel('Windgeschwindigkeit (m/s)')
plt.plot(Drehzahl, Windgeschwindigkeit, 'r')
plt.show()