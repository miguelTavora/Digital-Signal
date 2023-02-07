import numpy as np
from matplotlib import pyplot as plt

#Exercicio1

t=np.arange(121,123,0.01)
x= np.cos(540*np.pi*t+(np.pi/2))+np.cos(545*np.pi*t+(np.pi/2))


plt.plot(t,x, "g") #"g-" muda para cor verde
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("ex1.II-> " + r'$x(t)=cos(540\pi t+\frac{\pi}{2})+cos(545\pi t +\frac{\pi}{2})$')
plt.show()

