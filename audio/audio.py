import librosa
import numpy as np
import pydub
import os

class Audio(object):

    def __init__(self,):
        self.ruta = "/home/first_user/Web-Depresion/Web-Depresion/"
        pass

    def separar_voces(self):
        # Cargar el archivo de audio
        audio_file = pydub.AudioSegment.from_mp3(os.path.abspath('prueba.mp3'))

        # Convertir a formato de matriz de numpy
        audio_array = np.array(audio_file.get_array_of_samples())

        # Extraer las características del audio
        spectrogram = librosa.amplitude_to_db(np.abs(librosa.stft(audio_array)))

        # Detectar las voces en el audio
        vocals = librosa.decompose.decompose(spectrogram, n_components=2)[1]

        # Encontrar los intervalos de tiempo en los que la segunda persona habla
        threshold = np.mean(vocals) + 3 * np.std(vocals)  # Ajustar el umbral de detección
        speech_intervals = librosa.util.frame(vocals > threshold, hop_length=512)
        speech_times = librosa.frames_to_time(np.where(np.any(speech_intervals, axis=0))[0], sr=audio_file.frame_rate)

        # Imprimir los intervalos de tiempo en los que la segunda persona habla
        for i in range(0, len(speech_times), 2):
            print(f"La segunda persona habla entre {speech_times[i]:.2f}s y {speech_times[i+1]:.2f}s")

audio = Audio()
audio.separar_voces()