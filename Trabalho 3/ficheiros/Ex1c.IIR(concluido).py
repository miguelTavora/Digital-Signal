import scipy.signal as sg
import numpy as np
import matplotlib.pyplot as plt


n=np.arange(-6,6,0.001)
x = 10 + 2*np.cos((np.pi/6)*n)+ 10*np.cos((np.pi/3)*n)

#Para r= 0.9 e c=1

r = 0.9
c = 1
a11 = [1,r]
b11 = [1]
w,S11=sg.freqz(b11,a11)
plt.figure(facecolor="w", figsize=(12,8))

y11 = sg.lfilter(b11,a11,x)
plt.subplot(3,1,1)
plt.grid()
plt.title('y2[n] = x[n]-0.9y2[n-1]')
plt.xlabel('n',fontsize=10)
plt.ylabel('y(n)',fontsize=10)
plt.plot(n,y11,'#8B008B')


# ------------------------------------

#Para r=0.1 e c=1

r=0.1
c=1
a12 = [1,r]
b12 = [1]
w,S12=sg.freqz(b12,a12)

y12=sg.lfilter(b12,a12,x)
plt.subplot(3,1,2)
plt.grid()
plt.title('y2[n] = x[n]-0.1y2[n-1]')
plt.xlabel('n',fontsize=10)
plt.ylabel('y(n)',fontsize=10)
plt.plot(n,y12,'c')


# ------------------------------------

#Parar=-0.9 e c=1

r= -0.9
c=1
a13 = [1,r]
b13 = [1]
w,S13=sg.freqz(b13,a13)
y13=sg.lfilter(b13,a13,x)

plt.subplot(3,1,3)
plt.grid()
plt.title('y2[n] = x[n]+0.9y2[n-1]')
plt.xlabel('n',fontsize=10)
plt.ylabel('y(n)',fontsize=10)
plt.plot(n,y13)

plt.subplots_adjust(hspace=1)
plt.show()


# ------------------------------------

#Para r=0.9 e c=2

r=0.9
c=2
a21 = [1,0,r]
b21 = [1]
w,S21=sg.freqz(b21,a21)
plt.close("all")
plt.figure(facecolor="w", figsize=(12,8))
y21=sg.lfilter(b21,a21,x)

plt.subplot(3,1,1)
plt.grid()
plt.title('y2[n] = x[n]-0.9y2[n-2]')
plt.xlabel('n',fontsize=10)
plt.ylabel('y(n)',fontsize=10)
plt.plot(n,y21,'#8B008B')


# ------------------------------------

#Para r=0.1 e c=2

r=0.1
c=2
a22 = [1,0,r]
b22 = [1]
w,S22=sg.freqz(b22,a22)
y22=sg.lfilter(b22,a22,x)

y = sg.lfilter(b22,a22,x)
plt.subplot(3,1,2)
plt.grid()
plt.title('y2[n] = x[n]-0.1y2[n-2]')
plt.xlabel('n',fontsize=10)
plt.ylabel('y(n)',fontsize=10)
plt.plot(n,y22,'c')


# ------------------------------------

#Para r=-0.9 e c=2

r=-0.9
c=2
a23 = [1,0,r]
b23 = [1]
w,S23=sg.freqz(b23,a23)
y23=sg.lfilter(b23,a23,x)

plt.subplot(3,1,3)
plt.grid()
plt.title('y2[n] = x[n]+0.9y2[n-2]')
plt.xlabel('n',fontsize=8)
plt.ylabel('y(n)',fontsize=8)
plt.plot(n,y23)

plt.subplots_adjust(hspace=0.5)
plt.show()
