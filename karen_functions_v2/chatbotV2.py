import numpy as np 
import pandas as pd
from keras.preprocessing.text import Tokenizer
from keras.models import load_model
import pickle
from keras.preprocessing.sequence import pad_sequences
from keras.layers import Embedding
import re
from nltk.stem import WordNetLemmatizer
from karen_functions_v2.data_loader import Load_tokenizer,Load_maxlen
from karen_functions_v2.chatbot_functional import Functional
from karen_functions_v2.chatbot_non_functional import Non_Functional

#-------------------------------------------------------------------------------------------------------------------------

class Karen:

    def __init__(self):

        # load Lemmatizer
        self.lemmatizer = WordNetLemmatizer()
        # load tokenizer
        self.tokenizer = Load_tokenizer()
        # load functional model
        self.model = load_model(r'D:\vs code\python\DeepLearning\Projects\Karen\v2\models\cb2.h5')
        # load non functional model
        self.functional = Functional()
        self.non_functional = Non_Functional()



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


    def vectorise(self,sentence):
        # tokenizer = Load_tokenizer()

        sentence = self.preprocessing(sentence)

        sequence = self.tokenizer.texts_to_sequences([sentence])

        padded_sentences = pad_sequences(sequence,Load_maxlen())

        return padded_sentences


    #------------------------------------------------------------------------------------------------------------------------------------


    def ChatBot(self,sentence,reduce_retracing=True):
        # model_1 = load_model(r'D:\vs code\python\DeepLearning\Projects\Karen\v2\models\cb2.h5')
        # print("MODEL 1 LOADED CORRECTLY")
        sentence1 = self.vectorise(sentence)
        # print("SENTENCE VECTORISATION SUCCESSFUL")
        y = self.model.predict(sentence1)
        # print("MODEL PREDICTION SUCCESSFUL")
        predicted_class_index = int(np.argmax(y, axis=-1))
        # print("PRINTING THE PREDICTED cLASS",predicted_class_index)
        if predicted_class_index == 0:
            # print("EXECUTING FUNCTIONAL MODEL")
            self.functional.exec_func(sentence)
        else:
            # print("EXECUTING NON FUNCTIONAL MODEL")
            self.non_functional.exec_non_func(sentence)
#---------------------------------------------------------------------------------------------------------------------------------------