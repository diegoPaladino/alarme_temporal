#rede_neural

import random
import numpy as np

def derivada(n):
    return n*(1-n)

x = 0.85
y = 0.25
w = random.random()

#epocas

for i in range(54):
    a = np.tanh(x*w)

    e = y-a #ERRO

    w=x*derivada(e)

    print(a)