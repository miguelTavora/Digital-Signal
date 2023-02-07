import numpy as np
import scipy.signal as ss
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

Fs = 1000

Fs,musica = wav.read('musica.wav')

#Alínea A (filtro passa-baixo)

bka = ss.firwin(1001, (Fs/2.)/3., pass_zero = True, nyq = Fs/2.0)
wa,ha = ss.freqz(bka, [1.0])
plt.subplot(3,1,1)
plt.subplots_adjust(hspace = 0.5)
plt.grid()
plt.title(r'filtro passa-baixo($\omega_c = \frac{\pi}{3}$)')
plt.xlabel('n',fontsize=10)
plt.ylabel('y(n)',fontsize=10)
plt.plot(wa / np.pi * Fs/2.0, np.abs(ha),'#8B008B')

#Alínea B (filtro  passa-alto)

bkb = ss.firwin(1001, (Fs/2.)/3., pass_zero = False, nyq = Fs/2.0)
wb,hb = ss.freqz(bkb, [1.0])
plt.subplot(3,1,2)
plt.subplots_adjust(hspace = 0.5)
plt.grid()
plt.title(r'filtro passa-alto($\omega_c = \frac{\pi}{3}$)')
plt.xlabel('n',fontsize=10)
plt.ylabel('y(n)',fontsize=10)
plt.plot(wb / np.pi * Fs/2.0, np.abs(hb),'c')

#Alíena C filtro passa-banda entre pi/4 e pi/3

bkc = ss.firwin(1001,[(Fs/2.)/4.,(Fs/2.)/3.], pass_zero = False, nyq = Fs/2.0)
wc,hc = ss.freqz(bkc, [1.0])
plt.subplot(3,1,3)
plt.subplots_adjust(hspace = 0.5)
plt.grid()
plt.title(r'passa-banda entre ($\frac{\pi}{4}$ e $\frac{\pi}{3}$)')
plt.xlabel('n',fontsize=10)
plt.ylabel('y(n)',fontsize=10)
plt.plot(wc / np.pi * Fs/2.0, np.abs(hc),'r')

plt.subplots_adjust(hspace=1)
plt.show()


#Alínea D aplicar filtros em sinais wav's
plt.figure()
ak = [1.0]

#filtro a)

ya = ss.lfilter(bka,ak,musica)
plt.subplot(3,1,1)
plt.subplots_adjust(hspace = 0.5)
plt.grid()
plt.title(r'$\omega_c = \frac{\pi}{3}$')
plt.xlabel('n',fontsize=8)
plt.ylabel('y(n)',fontsize=8)
plt.plot(ya,'#8B008B')

#filtro b)

yb = ss.lfilter(bkb,ak,musica)
plt.subplot(3,1,2)
plt.subplots_adjust(hspace = 0.5)
plt.subplots_adjust(hspace = 0.5)
plt.grid()
plt.title(r'$\omega_c = \frac{\pi}{3}$')
plt.xlabel(r'n',fontsize=8)
plt.ylabel('y(n)',fontsize=8)
plt.plot(yb,'c')

#filtro c)

yc = ss.lfilter(bkc,ak,musica)
plt.subplot(3,1,3)
plt.subplots_adjust(hspace = 0.5)
plt.subplots_adjust(hspace = 0.5)
plt.grid()
plt.title(r' $\frac{\pi}{4}$ e $\frac{\pi}{3}$')
plt.xlabel('n',fontsize=10)
plt.ylabel('y(n)',fontsize=10)
plt.plot(yc,'r')

plt.subplots_adjust(hspace=1)
plt.show()






