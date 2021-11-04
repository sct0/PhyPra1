import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp

def f(a,e1,e2):
    f = (a**2-(e1-e2)**2)/(4*a)
    return f

def e(e1,e2):
    e = e2-e1
    return e

def fehlerf(a,e,f1,f2):
    fehlerf = np.sqrt((0.25*(1 + (e/a)**2))**2 * f1 **2 + (e/(2*a))**2*0.1**2)
    return fehlerf
         
#Bild bei 195cm
#Gegenstand bei 135cm
#F = 15cm

blau1 = np.array([152.6,153.0,152.4,152.3])

blau2 = np.array([170.7,170.8,171.5,171.0])

rot1 = np.array([153.2,153,152.5,152.7])

rot2 = np.array([170.4,170.5,170.2,170.5])

lb1 = np.array([153.1,152.8,152.6,153.0])

lb2 = np.array([170.4,170.5,170.2,170.5])

rb1 = np.array([153.1,153.3,152.7,153.1])

rb2 = np.array([170.6,170.5,170.7,171.0])

a = (195-135)

fehler = 0.15 #Fehler Maßstab: 0.5mm, Fehler Winkel Linse, Schirm, Bild: ~150*sin(0.5) = ~1mm

mblau1 = np.mean(blau1)
mblau2 = np.mean(blau2)
mrot1 = np.mean(rot1)
mrot2 = np.mean(rot2)
mlb1 = np.mean(lb1)
mlb2 = np.mean(lb2)
mrb1 = np.mean(rb1)
mrb2 = np.mean(rb2)

fblau = f(a,mblau1,mblau2)
frot = f(a,mrot1,mrot2)
flb = f(a,mlb1,mlb2)
frb = f(a,mrb1,mrb2)

fehlerm = fehler/np.sqrt(4)
fehlere = np.sqrt(fehlerm**2 + fehlerm**2)



print(fehlerm)

print(e(mblau1,mblau2))
print(e(mrot1,mrot2))
print(e(mlb1,mlb2))
print(e(mrb1,mrb2))

print(fblau)
print(frot)
print(flb)
print(frb)

print(fehlere)

print(fehlerf(a,e(mblau1,mblau2),fehler,fehlere))
print(fehlerf(a,e(mrot1,mrot2),fehler,fehlere))
print(fehlerf(a,e(mlb1,mlb2),fehler,fehlere))
print(fehlerf(a,e(mrb1,mrb2),fehler,fehlere))

