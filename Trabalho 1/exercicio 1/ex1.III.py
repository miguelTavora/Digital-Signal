import numpy as np
from matplotlib import pyplot as plt

#Exercicio1


t = np.arange(31,33,0.001)
x=(1/3+((2/3)*np.cos(5*np.pi*t)))*(np.cos(100*np.pi*t))


plt.plot(t,x, "r") #"r" muda para cor vermelha
plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("ex.1.III-> "+
          r'$x(t)=(\frac{1}{3}+\frac{2}{3}cos(5\pi t))*cos(100\pi t)$')

plt.show()
