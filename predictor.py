from collections import defaultdict
import string
import random

# Clase de Cadena de Markov
class Markov():
    # Constructor
    def __init__(self, file_path):
        self.file_path = file_path              # Ruta del archivo
        
        # Limpiamos el texto quitando las puntuaciones
        self.text = self.remove_punctuations(self.get_text())

        # Proceso interno del objeto
        self.model = self.model()
        
    # Obtenemos el texto de la ruta
    def get_text(self):
        '''
        This function will read the input file and return the text associated to the file line by line in a list
        '''
        text = []
        for line in open(self.file_path):
            text.append(line)
        return ' '.join(text)
    
    # Limpia el texto removiendo las puntuaciones
    def remove_punctuations(self, text):
        '''
        Given a string of text this function will return the same input text without any punctuations
        '''
        return text.translate(str.maketrans('','', string.punctuation))
    
    # Modelo para obtener el diccionario 
    def model(self):
        '''
        This function will take a block of text as the input and map each word in the text to a key where the
        values associated to that key are the words which proceed it

        args:
            text (String) : The string of text you wish to train your markov model around

        example:
            text = 'hello my name is V hello my name is G hello my current name is F world today is a good day'
            markov_model(text)
            >> {'F': ['world'],
                'G': ['hello'],
                'V': ['hello'],
                'a': ['good'],
                'current': ['name'],
                'good': ['day'],
                'hello': ['my', 'my', 'my'],
                'is': ['V', 'G', 'F', 'a'],
                'my': ['name', 'name', 'current'],
                'name': ['is', 'is', 'is'],
                'today': ['is'],
                'world': ['today']}
        '''

        # Separar el texto de entrada en palabras individuales con espacios
        words = self.text.split(' ')

        # Se crea un diccionario
        markov_dict = defaultdict(list)

        # Crear una lista de todos los pares de palabras
        for current_word, next_word in zip(words[0:-1], words[1:]):
            markov_dict[current_word].append(next_word)

        # Crea el diccionario
        markov_dict = dict(markov_dict)
        print('\nModelo entrenado satisfactoriamente')
        return markov_dict
# Fin de la clase Markov


# Funcion de prediccion de palabras dado el modelo de markov
def predict_words(chain, first_word, number_of_words=5):
    '''
    Given the input result from the markov_model function and the nunmber of words, this function will allow you to predict the next word
    in the sequence
    
    args:
        chain (Dictionary) : The result of the markov_model function
        first_word (String) : The word you want to start your prediction from, note this word must be available in chain
        number_of_words (Integer) : The number of words you want to predict
    
    example:
        chain = markov_model(text)
        generate_sentence(chain, first_word = 'do', number_of_words = 3)
        >> Do not fail.
    '''
    
    if first_word in list(chain.keys()):
        word1 = str(first_word)
        
        predictions = word1.capitalize()

        # Generate the second word from the value list. Set the new word as the first word. Repeat.
        for i in range(number_of_words-1):
            word2 = random.choice(chain[word1])
            word1 = word2
            predictions += ' ' + word2

        # End it with a period
        predictions += '.'
        return predictions
    else:
        return "La palabra no esta en el cuerpo"
  
if __name__ == '__main__':
    n_words = 40
    file_path = 'shrek.txt'

    # First word
    first_word = input("> Palabra base: ")
    # Number of words
    number_of_words = input("> Numero de palabras a generar: ")
    number_of_words = int(number_of_words)

    m = Markov(file_path)
    chain = m.model
    print("\nNúmero de palabras:", number_of_words, "\nTexto para entrenar: ", file_path ,"\nTexto predecido: \n")
    print(predict_words(chain, first_word, number_of_words))