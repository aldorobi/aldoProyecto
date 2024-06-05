# Bibliotecas de preprocesamiento de datos de texto
import nltk

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

import json
import pickle
import numpy as np

celsius = 32
fahrenheit = 2 * celsius
words = []
classes = []
word_tags_list = [""]
ignore_words = ["?","!",",",".","'s","'m","'"]
train_data_file = open('intents.json').read()
intents = json.loads(train_data_file)
# Función para añadir palabras raíz (steam words)
def get_stem_words(words,ignore_words):
    stem_words = []
    for word in words : 
        if word not in ignore_words :
                w = stemmer.stem(word.lower())
                stem_words.append(w)
            
    return stem_words 

for intent in intents ('intents'):
        
        for pattern in intent['patterns']:
              pattern_word = nltk.word_tokenize(pattern)
              words.extends(pattern_word)
              word_tags_list.append((pattern_word,intent['tag']))

        # Agregar todas las plabras de patrones a una lista
        if intent['tag'] not in classes : 
              classes.append(intent['tag'])
              stem_words = get_stem_words(words,ignore_words)
print(stem_words)
print(word_tags_list[0])
print(classes)
print (fahrenheit)
        # Agregar todas las etiquetas a la lista de clases
         

# Crear un corpus de palabras para el chatbot

