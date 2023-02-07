import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav


#Frequências de cada nota
notas_musicais = {'a': 27.5,'b': 30.86,'c': 32.7,'d': 36.7,'e': 41.2 , 'f':43.65 , 'g' : 48.9,
                  'a2': 55,'b2': 61.7,'c2': 65.4,'d2': 73.4,'e2': 82.4 , 'f2':87.3 , 'g2' : 97.9,
                  'a3': 110,'b3': 123.47,'c3': 130.8,'d3': 146.83,'e3': 164.8 , 'f3':174.6 , 'g3' : 196,
                  'a4': 220,'b4': 246.94,'c4': 261.63,'d4': 293.66,'e4': 329.63 , 'f4':349.23 , 'g4' : 392,
                  'a5': 440,'b5': 493.88,'c5': 523.25,'d5': 587.33,'e5': 659.26 , 'f5':698.46 , 'g5' : 783.99,'a6': 880}
         
#Composição da música que se pode ouvir (pode ser alterado)
composicao =[('d4',2),('a4',3),('e4',1),('b4',1),('g4',2),('f4',2),('e4',2),('f4',2)]



#Função que cria o sinal do som da composição 
def composicaoMusical(composicao,UnidadesTempo):

    print("unidade tempo: " + UnidadesTempo)
    frequencia_max = 0

    #for que encontra a maior frequência da composição para calcular a frequência de amostragem
    for n in composicao:
    
        frequencia = notas_musicais[n[0]]

        if (frequencia > frequencia_max):
            frequencia_max = frequencia

    fs = 5 * frequencia_max
    print(fs)
    frequencias = []

    musica = []

    #para cada uma das notas cria-se um sinal e faz-se hstack
    for n in composicao:
        t = np.arange(0,n[1],1/fs)
        nota = n[0]
        frequencia= notas_musicais[nota]
        frequencias.append(frequencia)
        x = 30000*np.cos(2*np.pi*frequencia*t)
        musica= np.hstack((musica,x))
    
    wav.write('Ex2.wav', int (fs),musica.astype('int16'))
    
    
    #Espectrograma
    plt.subplot(3,1,1)
    plt.specgram(musica,Fs = fs)
    

    #Espectros
    F = np.fft.fft(musica)
    freqs = np.fft.fftfreq(len(F),1/fs)
    plt.subplot(3,1,2)
    plt.plot(freqs,np.abs(F)/len(F))#espectro de amplitude
    plt.subplot(3,1,3)
    plt.plot(freqs,np.angle(F))  
    plt.show()
    return frequencias


#Frequências instantâneas
unidades = "segundos"
frequencias = composicaoMusical(composicao,unidades)
print(frequencias)



