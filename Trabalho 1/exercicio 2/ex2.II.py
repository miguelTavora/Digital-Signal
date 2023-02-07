import numpy as np
from matplotlib import pyplot as plt


#Exercio2


t=np.arange(-2,-1.53,0.00001)
u1 = np.zeros(len(t))
u1 [t+2 >= 0] = 1

u2= np.zeros(len(t))
u2 [t+1.53 >=0] = 1

x = (np.cos(2*np.pi*(15)*t))*(u1-u2)

plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("ex.2.II -> "+"$x(t)=cos(2\pi(15)t)(u(t+2)-u(t+1.53))$")
plt.grid()
plt.plot(t,x,"g")
plt.show()
