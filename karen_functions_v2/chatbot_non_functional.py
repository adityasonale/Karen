import random
import json
from karen_functions_v2.data_loader import Load_tokenizer_non_func,Load_labels_non_func,Load_maxlen_non_func
from keras.models import load_model
import numpy as np 
import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.models import load_model
import pickle
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding
import re
from nltk.stem import WordNetLemmatizer
from karen_functions_v2.Response import Speak


#-------------------------------------------------------------------------------------------------------------------------

class Non_Functional:

    def __init__(self):

        # initialise Sentence
        # lammatizer
        self.lemmatizer = WordNetLemmatizer()
        # tokenizer
        self.tokenizer = Load_tokenizer_non_func()
        # load non functional labels
        self.labels = Load_labels_non_func()
        # load non functional json
        self.intents = json.loads(open(r'D:\vs code\python\DeepLearning\Projects\Karen\v2\Datasets\non_functional\non_functional.json').read())
        # load non functional model
        self.model_functional = load_model(r"D:\vs code\python\DeepLearning\Projects\Karen\v2\models\cb2_non_functional.h5")


    def preprocessing(self,sentence):
        # lemmatizer = WordNetLemmatizer()
        sentence = sentence.lower()
        sentence = re.sub(r"i'm", "i am", sentence)
        sentence = re.sub(r"he's", "he is", sentence)
        sentence = re.sub(r"she's", "she is", sentence)
        sentence = re.sub(r"it's", "it is", sentence)
        sentence = re.sub(r"that's", "that is", sentence)
        sentence = re.sub(r"what's", "that is", sentence)
        sentence = re.sub(r"where's", "where is", sentence)
        sentence = re.sub(r"how's", "how is", sentence)
        sentence = re.sub(r"\'ll", " will", sentence)
        sentence = re.sub(r"\'ve", " have", sentence)
        sentence = re.sub(r"\'re", " are", sentence)
        sentence = re.sub(r"\'d", " would", sentence)
        sentence = re.sub(r"\'re", " are", sentence)
        sentence = re.sub(r"won't", "will not", sentence)
        sentence = re.sub(r"can't", "cannot", sentence)
        sentence = re.sub(r"n't", " not", sentence)
        sentence = re.sub(r"'til", "until", sentence)
        sentence = re.sub(r"who's", "who is", sentence)
        sentence = re.sub(r"[-()\"#/@;:<>{}`+=~|.\,?]", "", sentence)
        sentence = sentence.split()
        sentence = [self.lemmatizer.lemmatize(word) for word in sentence]
        sentence = [self.lemmatizer.lemmatize(word,pos='v') for word in sentence]
        sentence = ' '.join(sentence)

        return sentence  # string

    #-------------------------------------------------------------------------------------------------------------------------------


    def vectorise(self, sentence):
        # tokenizer = Load_tokenizer_non_func()

        sentence = self.preprocessing(sentence)

        sequence = self.tokenizer.texts_to_sequences([sentence])

        padded_sentences = pad_sequences(sequence,Load_maxlen_non_func())

        return padded_sentences


    #------------------------------------------------------------------------------------------------------------------------------------


    def exec_non_func(self, sentence):
        # labels = Load_labels_non_func() # create for functional and non functional
        # intents = json.loads(open(r'D:\vs code\python\DeepLearning\Projects\Karen\v2\Datasets\non_functional\non_functional.json').read())
        sentence = self.vectorise(sentence)
        # model_functional = load_model(r"D:\vs code\python\DeepLearning\Projects\Karen\v2\models\cb2_non_functional.h5")
        y = self.model_functional.predict(sentence)
        predicted_class_index = int(np.argmax(y, axis=-1))
        tag = self.labels[predicted_class_index]
        for intent in self.intents['intents']:
            if tag == intent["tag"]:
                reply = random.choice(intent['responses'])
                print(reply)
                Speak(reply)