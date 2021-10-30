import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

p1 = np.array([178.5,178.4,178.4,178.4,178.5])
p2 = np.array([178.4,178.5,178.3,178.5,178.5])

p = np.append(p1,p2)

mean = np.mean(p)
print(mean)

std = np.std(p)
print(std)

bw = 195 - mean

print(str(bw) + "+-" + str(std))