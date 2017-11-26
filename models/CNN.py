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
from keras.layers import Conv1D, MaxPooling1D, Embedding, Merge, Dropout
from keras.models import Model

max_seq_len = 1500
emd_dim = 100
val_split = 0.2

emails = []
labels = []

classes = []
class_labels = {}
class_ind = 0
print "6"

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

data = pad_sequences(sequences, maxlen=max_seq_len)

labels = to_categorical(np.asarray(labels))

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

embedding_matrix = np.random.random((len(word_index) + 1, emd_dim))
for word, i in word_index.items():
    embedding_vector = embeddings_index.get(word)
    if embedding_vector is not None:
        embedding_matrix[i] = embedding_vector
        
embedding_layer = Embedding(len(word_index) + 1,
                            emd_dim,
                            weights=[embedding_matrix],
                            input_length=max_seq_len,
                            trainable=True)

convs = []
filter_sizes = [3,4,5]

sequence_input = Input(shape=(max_seq_len,), dtype='int32')
embedded_sequences = embedding_layer(sequence_input)

for fsz in filter_sizes:
    l_conv = Conv1D(128, fsz, activation='relu')(embedded_sequences)
    l_pool = MaxPooling1D(5)(l_conv)
    convs.append(l_pool)
    
l_merge = Merge(mode='concat', concat_axis=1)(convs)
l_cov1 = Conv1D(128, 5, activation='relu')(l_merge)
l_pool1 = MaxPooling1D(5)(l_cov1)
l_drop_1 = Dropout(0.2)(l_pool1)
l_cov2 = Conv1D(128, 5, activation='relu')(l_drop_1)
l_pool2 = MaxPooling1D(30)(l_cov2)
l_drop_2 = Dropout(0.2)(l_pool2)
l_flat = Flatten()(l_drop_2)
l_dense = Dense(128, activation='relu')(l_flat)
l_drop_3 = Dropout(0.3)(l_dense)
preds = Dense(10, activation='softmax')(l_drop_3)

model = Model(sequence_input, preds)
model.compile(loss='categorical_crossentropy',
              optimizer='nadam',
              metrics=['acc'])

model.fit(x_train, y_train, validation_data=(x_val, y_val), 
            epochs=30, batch_size=10)
