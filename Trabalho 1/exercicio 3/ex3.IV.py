import numpy as np
from matplotlib import pyplot as plt


def soma(f0,t,N):
    x=np.zeros(t.shape)
    for k in np.arange(0,N+1):
        x= x+(8./np.power(np.pi,2))*(np.power(-1,k))*((np.sin(2*np.pi*(2.*k+1)*f0*t))/ (np.power((2.*k+1),2)))
    return x


def Graph():

    #N=1

    f0=0.25
    N=1
    n_periodos = 6.0

    plt.figure(facecolor = 'w', figsize =(12,8))


    tI=[0.0,n_periodos/f0]
    t= np.linspace(tI[0],tI[1],1e4)

    x=soma(f0, t, N)

    plt.close("all")

    plt.subplot(3,1,1)

    plt.plot(t,x,'k',linewidth = 3)
    plt.ylabel('N=1')
    plt.title('ex3.IV ->' +
    r'$x(t)=\frac {8}{\pi^2} \sum_{k=0}^{N}$ $(-1)^k$ $\frac{\sin(2\pi(2k+1)f_{0}t)}{(2k+1)^2}$')
    plt.grid()

    #N=10

    N=10

    x=soma(f0,t,N)

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
    plt.xlabel("t")
    plt.grid()


Graph()
plt.show()

    
