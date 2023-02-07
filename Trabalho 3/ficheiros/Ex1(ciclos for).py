import numpy as np
import scipy.signal as ss
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

c=[1,2]
r=[.9,.1,-.9]

def sistemaFIR(c,r):
    bk=[1.]
    ak=[1]
    for i in range(c):
        if (i>= 0 and i != c-1):
            bk.append(0)
        elif(i == c-1):
            bk.append(r)
        y=ss.freqz(bk,ak)

    return y

wF, hF = sistemaFIR(c[1], r[0])

def sistemaIIR(c,r):
    bk=[1]
    ak=[1.]
    for l in range(c):
        if (l >=0 and l != c-1):
            ak.append(.0)
        elif (l == c-1):
            ak.append(r)
        y=ss.freqz(bk,ak)

    return y

wI, hI = sistemaIIR(c[1], r[0])

plt.ylabel('|H(w)|')
plt.xlabel('w')
plt.plot(wI,np.abs(hI),'r')
plt.plot(wF,np.abs(hF))
plt.grid()
plt.show()

