import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import pysynth as pys
import pysynth_b as pysb
import pysynth_s as pyss
import pysynth_e as pyse


comp=[('d4',2),('a4',3),('e4',1),('b4',1),('g4',2),('f4',2),('e4',2),('f4',2)]

pys.make_wav(comp)
pysb.make_wav(comp)
pyss.make_wav(comp)
pyse.make_wav(comp)

plt.figure("Espectro A")
Fs, musica_a = wav.read('out.wav')
Z = np.fft.fft(musica_a)
freqs = np.fft.fftfreq(len(Z),1/Fs)
plt.subplot(2,1,1)
plt.plot(freqs,np.abs(Z)/len(Z))
plt.subplot(2,1,2)
plt.plot(freqs,np.angle(Z))

plt.figure("Espectro B")
Fs, musica_b = wav.read('outb.wav')
Z = np.fft.fft(musica_b)
freqs = np.fft.fftfreq(len(Z),1/Fs)
plt.subplot(2,1,1)
plt.plot(freqs,np.abs(Z)/len(Z))
plt.subplot(2,1,2)
plt.plot(freqs,np.angle(Z))

plt.figure("Espectro S")
Fs, musica_s = wav.read('outs.wav')
Z = np.fft.fft(musica_s)
freqs = np.fft.fftfreq(len(Z),1/Fs)
plt.subplot(2,1,1)
plt.plot(freqs,np.abs(Z)/len(Z))
plt.subplot(2,1,2)
plt.plot(freqs,np.angle(Z))

plt.figure("Espectro E")
Fs, musica_e = wav.read('oute.wav')
Z = np.fft.fft(musica_e)
freqs = np.fft.fftfreq(len(Z),1/Fs)
plt.subplot(2,1,1)
plt.plot(freqs,np.abs(Z)/len(Z))
plt.subplot(2,1,2)
plt.plot(freqs,np.angle(Z))

plt.figure("Espectrograma A")
plt.specgram(musica_a,Fs=Fs,NFFT=2048,noverlap=0)
axes = plt.gca()
axes.set_ylim([0,2500])


plt.show()

