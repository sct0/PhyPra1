#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 18:49:33 2021

@author: arne
"""

import numpy as np
import matplotlib.pyplot as plt

Pos = np.array([0,1,2,3,4,5])
x10 = np.array([124,117,116,71,51,22])
x20 = np.array([112,102,79,56,40,21])
x30 = np.array([92,71,59,35,32,20])
x10 = np.sqrt(2*x10/1.2)
x20 = np.sqrt(2*x20/1.2)
x30 = np.sqrt(2*x30/1.2)

plt.xlabel('Abstände vom Mittelpunkt (cm)')
plt.ylabel('Windgeschwindigkeit (m/s)')
plt.plot(Pos,x10)
plt.plot(Pos,x20)
plt.plot(Pos,x30)
plt.legend(['10cm','20cm','30cm'])