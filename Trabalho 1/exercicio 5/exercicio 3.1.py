import numpy as np
from matplotlib import pyplot as plt


def soma(θ):
    t = np.arange(0,2*np.pi,0.01)
    for θ in np.arange:
       x = (np.cos(θ))^2-((np.cos(2*θ)/4)-1/2)
    return x

def Graph():

    #θ = pi/3
    θ =(np.pi/3)
    t = np.arange(0,2*np.pi,0.01)
    x= soma(θ)
    plt.plot(t,x)

Graph()
plt.show()
    
       
       

