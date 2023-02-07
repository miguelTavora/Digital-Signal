import numpy as np
from matplotlib import pyplot as plt

#Exercicio4


n=np.linspace(0,32)

x=np.cos(2*np.pi*(n/16))


plt.stem(n,x,"k--")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.title("ex4.I -> " + r'$x[n]=cos[2\pi \frac{n}{16}]$')
plt.grid()
plt.show()
