import numpy as np
from matplotlib import pyplot as plt

#Exercicio4


n= np.linspace(-15,15)

x=np.exp(-(np.abs(n/3)))*np.cos(2*np.pi*(n/2))


plt.stem(n,x,"k")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.title("ex4.III")
plt.grid()
plt.show()


