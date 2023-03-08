import speech_recognition as sr

filename = "nueva/prub.0.wav"

# initialize the recognizer
r = sr.Recognizer()

# use the audio file as the audio source
with sr.AudioFile(filename) as source:
    # read the audio data from the file
    audio_data = r.record(source)

# recognize speech using Google Speech Recognition
text = r.recognize_google(audio_data, language='es-ES')

# print the recognized text
print(text)

