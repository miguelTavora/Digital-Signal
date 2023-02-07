import numpy as np
from matplotlib import pyplot as plt


#Exercio2


t=np.arange(-5,-1,0.01)
u1 = np.zeros(len(t))
u1 [-2*t-4 >= 0] = 1

u2 = np.zeros(len(t))
u2 [-t-4 >= 0] = 1

x = u1-u2

plt.xlabel("t")
plt.ylabel("x(t)")
plt.title("ex.2.I-> " + "x(t)=u(-2t-4)-u(-t-4)")
plt.grid()
plt.plot(t,x)
plt.show()
