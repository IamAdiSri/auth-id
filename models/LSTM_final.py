import numpy as np
import cPickle
from collections import defaultdict
import re

import sys
import os

os.environ['KERAS_BACKEND']='tensorflow'

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils.np_utils import to_categorical

from keras.layers import Embedding
from keras.layers import Dense, Input, Flatten
from keras.layers import Conv1D, MaxPooling1D, Embedding, Merge, Dropout, GRU, LSTM, Bidirectional
from keras.models import Model

max_sen_len = 1500
emb_dim = 100
val_split = 0.2

emails = []
labels = []

classes = []
class_labels = {}
class_ind = 0

for author_dir in os.listdir('clean_enron'):
    if author_dir == '.DS_Store':
        continue
    classes.append(author_dir)
    class_labels[author_dir] = class_ind
    class_ind += 1

for author_dir in os.listdir('clean_enron'):
    if author_dir == '.DS_Store':
        continue
    for message_file in os.listdir('./clean_enron/' + author_dir):
        with open('./clean_enron/' + author_dir + '/' + message_file, 'r') as f:
            text = f.read()
            text = text.replace("\n", " ")
            emails.append(text.lower())
            labels.append(class_labels[author_dir])    

tokenizer = Tokenizer()
tokenizer.fit_on_texts(emails)
sequences = tokenizer.texts_to_sequences(emails)

word_index = tokenizer.word_index

data = pad_sequences(sequences, maxlen=max_sen_len)

labels = to_categorical(np.asarray(labels))
print labels.shape[0], labels.shape[1]

indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]
nb_validation_samples = int(val_split * data.shape[0])

x_train = data[:-nb_validation_samples]
y_train = labels[:-nb_validation_samples]
x_val = data[-nb_validation_samples:]
y_val = labels[-nb_validation_samples:]

embeddings_index = {}
with open('glove.6B.100d.txt') as f:
    for line in f:
        values = line.split()
        word = values[0]
        coefs = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = coefs

embedding_matrix = np.random.random((len(word_index) + 1, emb_dim))
for word, i in word_index.items():
    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        embedding_matrix[i] = embedding_vector
        
embedding_layer = Embedding(len(word_index) + 1,
                            emb_dim,
                            weights=[embedding_matrix],
                            input_length=max_sen_len,
                            trainable=True)

sequence_input = Input(shape=(max_sen_len,), dtype='int32')
embedded_sequences = embedding_layer(sequence_input)
l_lstm = Bidirectional(LSTM(100))(embedded_sequences)
dense_1 = Dense(128, activation="relu")(l_lstm)
drop_1 = Dropout(0.3)(dense_1)
preds = Dense(10, activation='softmax')(drop_1)
model = Model(sequence_input, preds)
model.compile(loss='categorical_crossentropy',
              optimizer='rmsprop',
              metrics=['acc'])

model.fit(x_train, y_train, validation_data=(x_val, y_val),
          epochs=30, batch_size=50)
