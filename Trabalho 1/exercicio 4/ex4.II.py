import numpy as np
from matplotlib import pyplot as plt

#Exercicio4



n=np.linspace(-50,50)

x=(10/(np.pi*n))*np.sin((np.pi*n)/10)


plt.stem(n,x,"g")
plt.xlabel("n")
plt.ylabel("x[n]")
plt.title("ex4.II -> "
          + r'$x[n]=\frac{10}{\pi n}sin[\frac{\pi n}{10}] , x[0] = 1$')
plt.grid()
plt.show()
