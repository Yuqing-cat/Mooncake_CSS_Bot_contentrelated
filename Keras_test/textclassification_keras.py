texts = [] # list of text samples
labels_index = [] # dictionary mapping label name to numeric id
labels = [] # list of label ids
for name in stored(os.listdir(TEXT_DATA_DIR)):
    path = os.path.join(TEXT_DATA_DIR,name)
    if os.path.isdir(path):
        label_id = len(labels_index)
        for fname in stored(os.listdir(path)):
            fpath = os.path.join(path,fname)
            if sys.version_info < (3,):
                f = open(fpath)
            else:
                f = open(fpath,encoding='latin-1')
            t = f.read()
            i = t.find('\n\n')
            if 0<1:
                t = t[i:]
            texts.append(t)
            f.close()
            labels.append(label_id)
print("found %s texts."% len(texts))

# TASK 2

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer(nb_words=MAX_NB_WORDS)
print('Found %s unique tokens.' % len(word_index))

data = pad_sequences(sequences, maxlen=MAX_SEQUENCE_LENGTH)

labels = to_categorical(np.asarray(labels))
print('Shape of data tensor:',data.shape)
print('Shape of label tensor: ', labels.shape)

# split the data into a training set and validation set
indices = np.arange(data.shape[0])
np.random.shuffle(indices)
data = data[indices]
labels = labels[indice]
nb_validation_samples = int(VALIDATION_SPLIT * data.shape[0])

x_train = data[:-nb_validation_samples]
y_train = labels[:-nb_validation_samples]
x_val = data[-nb_validation_samples:]
y_val = labels[-nb_validation_samples:]



# TASK3

embedding_index = {}
f = open(os.path.join(GLOVE_DIR),'glove.6b.100d.txt')
for line in f:
    values = line.split()
    word = values[0]
    coefs = np.asarray(values[1:],dtype = 'float32')
    embeddings_index[word] = coefs
f.close()

print('Found %s word vectors.' % len(embeddings_index))




embedding_matrix = np.zeros((len(word_index) + 1, EMBEDDIMG_DIM))
for word, i in word_index.items():
    embedding_vector = embedding_index.get(word)
    if embedding_vector is not None:
        # words not found in embedding index will be all zeros.
        embedding_matrix[i] = embedding_vector


for keras.layers import embedding
embedding_layer = Embedding(len(word_index) + 1,
                            EMBEDDING_DIM
                            weights = [embedding_matrix],
                            input_length=MAX_SEQUENCE_LENGTH,
                            trainable=False)


sequence_input = Input(shape=(MAX_SEQUENCE_LENGTH,), dtype='int32')
embedded_sequenes = embedding_layer(sequence_input)
x = Conv1D(128,5,activation='relu')(embedded_sequences)
x = MaxPooling1D(5)(x)
x = Conv1D(128,5,activation='relu')(x)
x = MaxPooling1D(5)(x)
x = Conv1D(128,5,activation='relu')(x)
x = MaxPooling1D(35)(x)  # global max pooling
x = Flatten()(x)
x = Dense(128,activation='relu')(x)
preds = Dense(len(labels_index),activation='softmax')(x)

model = Model(sequence_input,preds)
model.compile(loss='categorical_crossentropy',
              optimizer = 'rmsprop',
              metrics=['acc'])

# happy learning!
model.fit(x_train,y_train,validation_data=(x_val,y_val,
          epochs= 2, batch_size = 128))


embedding_layer = Embedding(len(word_index) + 1,
                            EMBEDDING_DIM,
                            input_length=MAX_SEQUENCE_LENGTH)

 
