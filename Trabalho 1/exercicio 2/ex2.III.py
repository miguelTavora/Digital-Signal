import numpy as np
from matplotlib import pyplot as plt


#Exercio2


t=np.arange(-0.5,0.5,0.001)

u1=np.zeros(len(t))
u1 [t+1 >= 0] = 1
    

u2=np.zeros(len(t))
u2 [t-1 >=0] = 1

x= 2*np.cos(2*np.pi*(50)*t)*np.exp(-20*t**2)*(u1-u2)

plt.plot(t,x,'r')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.title('ex2.III')
plt.grid()
plt.show()

