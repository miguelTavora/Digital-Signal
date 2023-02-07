import scipy.signal as sg
import numpy as np
import matplotlib.pyplot as plt


#Para r= 0.9 e c=1

r = 0.9
c = 1
a11 = [1]
b11 = [1,r]
w,S11=sg.freqz(b11,a11)
plt.figure(facecolor="w", figsize=(12,8))

plt.subplot(3,1,1)
plt.grid()
plt.title('Sistema11(Filtro Passa-baixo)', fontsize=10)
plt.xlabel('n',fontsize=10)
plt.ylabel('y(n)',fontsize=10)
plt.plot(w, np.abs(S11),'#8B008B')


# ------------------------------------

#Para r=0.1 e c=1

r=0.1
c=1
a12 = [1]
b12 = [1,r]
w,S12=sg.freqz(b12,a12)

plt.subplot(3,1,2)
plt.grid()
plt.title('Sistema12(Filtro Passa-baixo)')
plt.xlabel('n',fontsize=10)
plt.ylabel('y(n)',fontsize=10)
plt.plot(w, np.abs(S12),'c')


# ------------------------------------

#Parar=-0.9 e c=1

r= -0.9
c=1
a13 = [1]
b13 = [1,r]
w,S13=sg.freqz(b13,a13)

plt.subplot(3,1,3)
plt.grid()
plt.title('Sistema13(Filtro Passa-baixo)')
plt.xlabel('n',fontsize=10)
plt.ylabel('y(n)',fontsize=10)
plt.plot(w, np.abs(S13))

plt.subplots_adjust(hspace=1)
plt.show()


# ------------------------------------

#Para r=0.9 e c=2

r=0.9
c=2
a21 = [1]
b21 = [1,0,r]
w,S21=sg.freqz(b21,a21)
plt.close("all")
plt.figure(facecolor="w", figsize=(12,8))

plt.subplot(3,1,1)
plt.grid()
plt.title('Sistema21(Filtro Passa-banda')
plt.xlabel('n',fontsize=10)
plt.ylabel('y(n)',fontsize=10)
plt.plot(w, np.abs(S21),'#8B008B')


# ------------------------------------

#Para r=0.1 e c=2

r=0.1
c=2
a22 = [1]
b22 = [1,0,r]
w,S22=sg.freqz(b22,a22)

plt.subplot(3,1,2)
plt.grid()
plt.title('Sistema22(Filtro Passa-banda)')
plt.xlabel('n',fontsize=10)
plt.ylabel('y(n)',fontsize=10)
plt.plot(w, np.abs(S22),'c')


# ------------------------------------

#Para r=-0.9 e c=2

r=-0.9
c=2
a23 = [1]
b23 = [1,0,r]
w,S23=sg.freqz(b23,a23)

plt.subplot(3,1,3)
plt.grid()
plt.title('Sistema23(Filtro Passa-banda)')
plt.xlabel('n',fontsize=8)
plt.ylabel('y(n)',fontsize=8)
plt.plot(w, np.abs(S23))

plt.subplots_adjust(hspace=0.5)
plt.show()
