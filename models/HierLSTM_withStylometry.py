import numpy as np
import cPickle
from collections import defaultdict
import re
import random
import sys
import os

os.environ['KERAS_BACKEND']='tensorflow'

from keras.preprocessing.text import Tokenizer, text_to_word_sequence
from keras.preprocessing.sequence import pad_sequences
from keras.utils.np_utils import to_categorical

from keras.layers import Embedding
from keras.layers import Dense, Input, Flatten
from keras.layers import Conv1D, MaxPooling1D, Embedding, Merge, Dropout, LSTM, GRU, Bidirectional, TimeDistributed
from keras.layers.normalization import BatchNormalization
from keras.layers import merge
from keras.layers import concatenate

from keras.models import Model
from keras import backend as K
from keras.engine.topology import Layer, InputSpec
from keras.callbacks import Callback

max_sen_len = 100
max_sents = 30
emb_dim = 100
val_split = 0.2

lines = []
labels = []
texts = []
f_names = []
style_vectors = []
scd = []
style_dict = {}
classes = []
class_labels = {}
class_ind = 0
style_train = []
style_val = []

# Input the stylometric features 
with open("./extracted_features/stylometricVector.txt", "r") as sv:
    for line in sv:
        scd = line.split(',')
        s_key = scd[0] + "/" + scd[1]

        s_value = map(float, scd[2:])

        style_dict[s_key] = s_value

# Input the class labels
for author_dir in os.listdir('clean_enron'):
    if author_dir == '.DS_Store':
        continue
    classes.append(author_dir)
    class_labels[author_dir] = class_ind
    class_ind += 1

# Input the contents of each email
for author_dir in os.listdir('clean_enron'):
    if author_dir == '.DS_Store':
        continue
    for message_file in os.listdir('./clean_enron/' + author_dir):
        with open('./clean_enron/' + author_dir + '/' + message_file, 'r') as f:
            text = f.read()
            sentences = text.lower().split('\n')
            lines.append(sentences)  
            text = text.lower().replace("\n", " ")
            labels.append(class_labels[author_dir])
            texts.append(text)
            f_names.append(author_dir + '/' + message_file)
            if author_dir + '/' + message_file not in style_dict :
                style_vectors.append([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0 ])
            else :
                style_vectors.append(style_dict[ author_dir + '/' + message_file ])
            
# Convert stylometric feature vector to numpy array
style_vectors = np.array(style_vectors)

# Normalize the numerical feature vectors
style_vectors = style_vectors / style_vectors.max(axis=0)

#Tokenization
tokenizer = Tokenizer()
tokenizer.fit_on_texts(texts)
data = np.zeros((len(texts), max_sents, max_sen_len), dtype='int32')
for i, sentences in enumerate(lines):
    for j, sent in enumerate(sentences):
        if j< max_sents:
            wordTokens = text_to_word_sequence(sent)
            k = 0
            for _, word in enumerate(wordTokens):
                if k < max_sen_len:
                    data[i, j, k] = tokenizer.word_index[word]
                    k = k + 1                    
word_index = tokenizer.word_index
labels = to_categorical(np.asarray(labels))

# Randomly shuffle the data
indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = labels[indices]
style_vectors = style_vectors[indices]

# Split the data as training  and validation
nb_validation_samples = int(val_split * data.shape[0])
x_train = data[:-nb_validation_samples]
y_train = labels[:-nb_validation_samples]
x_val = data[-nb_validation_samples:]
y_val = labels[-nb_validation_samples:]
style_train = style_vectors[:-nb_validation_samples]
style_val = style_vectors[-nb_validation_samples:]

## Performance metrics

# F1 score
f1_scores = []

# Precision
precisions = []

# Recall
recalls = []

# Create embeddings
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
        # words not found in embedding index will be all-zeros.
        embedding_matrix[i] = embedding_vector
        
# Embedding layer
embedding_layer = Embedding(len(word_index) + 1,
                            emb_dim,
                            weights=[embedding_matrix],
                            input_length=max_sen_len,
                            trainable=True)

# Bidirectional LSTM
sentence_input = Input(shape=(max_sen_len,), dtype='int32')
embedded_sequences = embedding_layer(sentence_input)
l_lstm = Bidirectional(LSTM(100))(embedded_sequences)

# Bidirectional LSTM
sentEncoder = Model(sentence_input, l_lstm)
email_input = Input(shape=(max_sents,max_sen_len), dtype='int32')
email_encoder = TimeDistributed(sentEncoder)(email_input)
l_lstm_sent = Bidirectional(LSTM(100))(email_encoder)

# Input the stylometric feature
auxiliary_input = Input(shape=(8,))

# Concatenate with lstm output
x_new = concatenate([l_lstm_sent, auxiliary_input])

# Dense layer
dense_1 = Dense(128, activation='relu')(x_new)

# Dropout layer
drop_1 = Dropout(0.3)(dense_1)

# Final Dense layer
preds = Dense(10, activation='softmax')(drop_1)

# Model
model = Model(inputs=[email_input, auxiliary_input], outputs=preds)

# Compile the model
model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['acc'])

# Summarize the model
model.summary()

# Fit the model
model.fit(x=[x_train, style_train], y=y_train, validation_data=([x_val, style_val], y_val), epochs=30, batch_size=50)