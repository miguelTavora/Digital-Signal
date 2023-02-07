import numpy as np
from matplotlib import pyplot as plt

#Exercicio1


t=np.arange(-1,3,0.001)
x=2*np.cos(2*np.pi*10*t+(np.pi/4))+np.sin(2*np.pi*11*t-(np.pi/3))

plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("ex1.I-> "+r"$x(t)=2cos(2\pi10t+\frac{\pi}{4})+sin(2\pi11t-\frac{\pi}{3})$")
plt.plot(t,x)
plt.show()



