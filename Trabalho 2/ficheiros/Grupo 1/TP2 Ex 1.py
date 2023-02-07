import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav


#Função que gera o sinal referido e cria um ficheiro wav
def f_sinal(A,f,d): #A é a amplitude | f é a frequência | d é a duração
    fs = 4 * f #fs é 4 vezes a fmax
    ts = 1/fs
    t = np.arange(0,d,ts)
    x_t = A * np.cos(2*np.pi*f*t)
    wav.write('Ex1.wav',fs,x_t.astype('int16'))
    plt.subplot(4,1,1)
    plt.plot(t,x_t)


#Sinusóide com frequência e amplitude pedidas 
Frequencia = 447 #((43740+45102+45170)/3)/100 = 446.70
Amplitude = 30000 #Amplitude = 3 não se ouve
Duracao = 10
sinal = f_sinal(Amplitude,Frequencia,Duracao)


#Espectro do sinal
fs = 4 * Frequencia
ts = 1/fs
t = np.arange(0,Duracao,ts)
x_t = Amplitude * np.cos(2*np.pi*Frequencia*t)


F = np.fft.fft(x_t)
freqs = np.fft.fftfreq(len(F),ts)
plt.title("Sinal sinusoidal | Espectro de amplitude e fase | Espectograma")
plt.subplot(4,1,2)
plt.plot(freqs,np.abs(F)/len(F))
plt.subplot(4,1,3)
plt.plot(freqs,np.angle(F)) 


#Espectograma do sinal
plt.subplot(4,1,4)
plt.specgram(x_t, Fs = fs)
plt.show()

#Diferenças entre o Espectro e o Espectrograma

#O espectro é uma representação de um sinal no domínio da frequência
#que permite ver a relação entre esta e a amplitude/fase enquanto o
#espectrograma é uma forma de analisar o sinal em relação a tempo-frequência.
