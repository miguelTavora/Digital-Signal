import scipy.signal as sg
import numpy as np
import matplotlib.pyplot as plt


#Para r= 0.9 e c=1

r = 0.9
c = 1
a11 = [1,r]
b11 = [1]
w,S11=sg.freqz(b11,a11)
plt.figure(facecolor="w", figsize=(12,8))


plt.subplot(3,1,1)
plt.subplots_adjust(hspace=0.5)
plt.plot(w, np.abs(S11))
plt.title("Sistema11 (Filtro  Passa-alto)", fontsize=10)
plt.ylabel(r'$y[n](r=0.9, c=1)$', fontsize=10)
plt.xlabel('n',fontsize=10)
plt.grid()

# ------------------------------------

#Para r=0.1 e c=1

r=0.1
c=1
a12 = [1,r]
b12 = [1]
w,S12=sg.freqz(b12,a12)

plt.subplot(3,1,2)
plt.plot(w, np.abs(S12),'r', lw=4)
plt.title("Sistema12(Filtro Passa-alto)", fontsize=10)
plt.ylabel(r'$y[n](r=0.1, c=1)$', fontsize=10)
plt.xlabel('n',fontsize=10)
plt.grid()

# ------------------------------------

#Parar=-0.9 e c=1

r= -0.9
c=1
a13 = [1,r]
b13 = [1]
w,S13=sg.freqz(b13,a13)

plt.subplot(3,1,3)
plt.plot(w, np.abs(S13), 'k', lw=4)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.title("Sistema13(Filtro Passa-baixo)", fontsize=10)
plt.xlabel('n',fontsize=10)
plt.ylabel(r'$y[n](r=-0.9, c=1)$', fontsize=10)
plt.grid()
plt.show()

# ------------------------------------

#Para r=0.9 e c=2

r=0.9
c=2
a21 = [1,0,r]
b21 = [1]
w,S21=sg.freqz(b21,a21)
plt.close("all")
plt.figure(facecolor="w", figsize=(10,9))

plt.subplot(3,1,1)
plt.subplots_adjust(hspace=0.5)
plt.plot(w, np.abs(S21), lw=4)
plt.title("Sistema21(Filtro Passa-banda)", fontsize=10)
plt.xlabel('n',fontsize=10)
plt.ylabel(r'$y[n](r=0.9, c=2)$', fontsize=10)
plt.grid()


# ------------------------------------

#Para r=0.1 e c=2

r=0.1
c=2
a22 = [1,0,r]
b22 = [1]
w,S22=sg.freqz(b22,a22)

plt.subplot(3,1,2)
plt.plot(w, np.abs(S22),'r', lw=4)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.title("Sistema22(Filtro Passa-banda)", fontsize=10)
plt.xlabel('n',fontsize=10)
plt.ylabel(r'$y[n](r=0.1, c=2)$', fontsize=10)
plt.grid()

# ------------------------------------

#Para r=-0.9 e c=2

r=-0.9
c=2
a23 = [1,0,r]
b23 = [1]
w,S23=sg.freqz(b23,a23)

plt.subplot(313)
plt.plot(w, np.abs(S23),'k', lw=4)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.title("Sistema23(Filtro Passa-banda)", fontsize=10)
plt.xlabel('n',fontsize=10)
plt.ylabel(r'$y[n](r=-0.9, c=2)$', fontsize=10)
plt.grid()
plt.show()

