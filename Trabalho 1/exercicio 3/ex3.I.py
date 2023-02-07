import numpy as np
from matplotlib import pyplot as plt

#N = 1

f0 = 1
t = np.arange(0, 6, 0.001)
N = 1 
x = np.zeros(len(t))

for k in range (1, N+1) :
    x = x+ 4/np.pi*np.sin(2*np.pi+(2*k-1)*f0*t)/(2*k-1)

plt.plot(t, x,"k")


#N = 10

N = 10
y = np.zeros(len(t))

for k in range (1, N+1) :
    y = y+ 4/np.pi*np.sin(2*np.pi+(2*k-1)*f0*t)/(2*k-1)

plt.plot(t, y,"r")

#N = 10000

N = 10000
z = np.zeros(len(t))

for k in range (1, N+1) :
    z = z+ 4/np.pi*np.sin(2*np.pi+(2*k-1)*f0*t)/(2*k-1)

plt.plot(t, z)


plt.xlabel("t")
plt.ylabel("Black(N=1), Red(N=10), Blue(N=10000)")
plt.title('ex3.I-> '+ r'$x(t)=\frac{4}{\pi}$ $\sum_{k=1}^{N}$ $\frac{\sin(2\pi(2k-1)f_{0}t)}{2k-1}$')
plt.grid()
plt.show()
    

