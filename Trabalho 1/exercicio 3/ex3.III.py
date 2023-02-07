import numpy as np
from matplotlib import pyplot as plt


def soma(f0,t,N):
    x=np.zeros(t.shape)
    for k in np.arange(1,N+1):
        x= x+(np.sin(2*np.pi*k*f0*t)/k)
    x=x*2/np.pi
    return x


def Graph ():

    #N=1

    f0 = 1
    N = 1
    n_periodos = 6.0

    plt.figure(facecolor = 'w', figsize = (12,8))

    tI=[0.0,n_periodos/f0]
    t=np.linspace(tI[0],tI[1],1e4)

    x=soma(f0, t, N)

    plt.close("all")

    plt.subplot(3,1,1)

    plt.plot(t,x,'k',linewidth = 3)
    plt.ylabel('N = 1')
    plt.title('ex3.III ->' +
    r'$x(t)=\frac{2}{\pi} \sum_{k=1}^{N}$ $\frac{\sin(2\pi k f_{0}t)}{k}$')
    plt.grid()

    #N=10

    N=10

    x = soma(f0,t,N)

    plt.subplot(3,1,2)
    plt.plot(t,x,'r',linewidth = 3)
    plt.ylabel("N=10")
    plt.grid()

    #N=10000

    N=10000

    x=soma(f0,t,N)

    plt.subplot(3,1,3)
    plt.plot(t,x,linewidth = 3)
    plt.ylabel("N=10000")
    plt.grid()
    plt.xlabel("t")

Graph()
plt.show()
    
    

    
    
