import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt

notas = {'a': 27.5,'b': 30.86,'c': 32.7,'d': 36.7,'e': 41.2 , 'f':43.65 , 'g' : 48.9, 'a2': 55,'b2': 61.7,
        'c2': 65.4,'d2': 73.4,'e2': 82.4 , 'f2':87.3 , 'g2' : 97.9,'a3': 110,'b3': 123.47,'c3': 130.8,
        'd3': 146.83,'e3': 164.8 ,'f3':174.6 , 'g3' : 196,'a4': 220,'b4': 246.94,'c4': 261.63,'d4': 293.66,
        'e4': 329.63 , 'f4': 349.23 , 'g4' : 392,'a5': 440,'b5': 493.88,'c5': 523.25,'d5': 587.33,'e5': 659.26 ,
        'f5': 698.46 , 'g5' : 783.99,'a6': 880,'b6': 987.77,'c6': 1046.5,'d6': 1174.7,'e6': 1318.5 , 'f6':1396.9 ,
        'g6' : 1568}

Fs, musica = wav.read("Ex2.wav")
espectro = np.fft.fft(musica)
spect, f, t, ii = plt.specgram(musica, Fs = Fs, NFFT=512, noverlap = 0)

def Sem_duplicados(x):
        i = 1
        while i < len(x):    
                if x[i] == x[i-1]:
                        x.pop(i)
                        i = i - 1  
                i = i + 1
        return x

frequencia_notas = []
for a in range(0, spect.shape[1], 1):
	plt.plot(f,spect[:,a])
	frequencia_notas.append(format(3.8399*np.argmax(spect[:,a]),'.2f'))

frequencia_notas = Sem_duplicados(frequencia_notas)

print(frequencia_notas)
