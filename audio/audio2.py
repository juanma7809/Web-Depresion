import librosa
import numpy as np
import os

class Audio(object):

    def __init__(self,):
        pass

    def separar_voces(self):
        # Cargar el archivo de audio
        archivo_audio = os.path.abspath("prueba4.mp3")
        audio, sr = librosa.load(archivo_audio)

        # Extraer características de audio
        mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=20)

        # Transponer el arreglo de características de audio para obtener los coeficientes MFCC en filas
        mfccs = np.transpose(mfccs)

        # Calcular la media y la desviación estándar de los coeficientes MFCC
        media = np.mean(mfccs, axis=0)
        desviacion_estandar = np.std(mfccs, axis=0)

        # Normalizar los coeficientes MFCC
        mfccs_norm = (mfccs - media) / desviacion_estandar

        # Aplicar algoritmo K-Means para separar en clusters
        from sklearn.cluster import KMeans

        num_clusters = 2
        kmeans = KMeans(n_clusters=num_clusters, random_state=0).fit(mfccs_norm)

        # Obtener las etiquetas de los clusters
        etiquetas_clusters = kmeans.labels_

        # Calcular la duración de cada trama de audio
        duracion_trama = librosa.get_duration(y=audio) / mfccs.shape[0]

        # Calcular los intervalos de tiempo en los que se detectó la segunda persona
        umbral = 0.5  # umbral para considerar que un cluster corresponde a la segunda persona
        inicio = 0
        intervalos_segunda_persona = []
        for i in range(1, len(etiquetas_clusters)):
            if etiquetas_clusters[i] == 1 and etiquetas_clusters[i-1] == 0:
                inicio = (i-1) * duracion_trama
            elif etiquetas_clusters[i] == 0 and etiquetas_clusters[i-1] == 1:
                final = i * duracion_trama
                if final - inicio >= umbral:
                    intervalos_segunda_persona.append((inicio, final))

        # Imprimir los intervalos de tiempo
        for intervalo in intervalos_segunda_persona:
            print(f"La segunda persona habló desde {intervalo[0]:.2f} segundos hasta {intervalo[1]:.2f} segundos.")


audio = Audio()
audio.separar_voces()