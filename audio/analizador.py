import nltk

# Descargar el paquete de datos requerido por NLTK
nltk.download('punkt')

# Cargar el archivo de texto que contiene la conversación
with open('conversacion.txt', 'r') as f:
    conversation = f.read()

# Tokenizar el texto en oraciones
sentences = nltk.sent_tokenize(conversation)

# Iterar sobre cada oración y determinar quién la dijo
person1_sentences = []
person2_sentences = []

for sentence in sentences:
    # Tokenizar la oración en palabras
    words = nltk.word_tokenize(sentence)
    
    # Si la primera palabra de la oración es el nombre de la primera persona,
    # se agrega la oración a la lista de oraciones de la primera persona.
    if words[0] == 'Persona1':
        person1_sentences.append(sentence)
    # Si no, se agrega a la lista de oraciones de la segunda persona.
    else:
        person2_sentences.append(sentence)

# Imprimir las oraciones de cada persona
print("Oraciones de la Persona 1:")
for sentence in person1_sentences:
    print(sentence)

print("Oraciones de la Persona 2:")
for sentence in person2_sentences:
    print(sentence)
