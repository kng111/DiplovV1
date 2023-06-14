
import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.layers import Activation, Dense, LSTM

def stih():
    for i in range(1):
    

        dt = ['input1.txt','input2.txt','input3.txt','input4.txt','input5.txt','input6.txt','input7.txt','input8.txt','input9.txt','input10.txt','input11.txt']
        text = open(f'{random.choice(dt)}', 'rb')\
            .read().decode(encoding='utf-8').lower()



        # print(text)
        text = text[10:160500]
        # text = text[100:36500]




        characters = sorted(set(text))
        # print(characters)



        char_to_index = dict((c, i) for i, c in enumerate(characters))
        index_to_char = dict((i, c) for i, c in enumerate(characters))

        SEQ_LENGTH = 60
        STEP_SIZE = 3

        sentences = []
        next_char = []

        for i in range(0, len(text) - SEQ_LENGTH, STEP_SIZE):
            sentences.append(text[i: i + SEQ_LENGTH])
            next_char.append(text[i + SEQ_LENGTH])

        x = np.zeros((len(sentences), SEQ_LENGTH,
                    len(characters)), dtype=np.bool)
        y = np.zeros((len(sentences),
                    len(characters)), dtype=np.bool)

        for i, satz in enumerate(sentences):
            for t, char in enumerate(satz):
                x[i, t, char_to_index[char]] = 1
            y[i, char_to_index[next_char[i]]] = 1

        model = Sequential()
        model.add(LSTM(128,
                    input_shape=(SEQ_LENGTH,
                                    len(characters))))
        model.add(Dense(len(characters)))
        model.add(Activation('softmax'))

        model.compile(loss='categorical_crossentropy',
                    optimizer=RMSprop(lr=0.01))

        model.fit(x, y, batch_size=256, epochs=6)

        def sample(preds, temperature=1.0):
            preds = np.asarray(preds).astype('float64')
            preds = np.log(preds) / temperature
            exp_preds = np.exp(preds)
            preds = exp_preds / np.sum(exp_preds)
            probas = np.random.multinomial(1, preds, 1)
            return np.argmax(probas)


        def generate_text(length, temperature):
            start_index = random.randint(0, len(text) - SEQ_LENGTH - 1)
            generated = ''
            sentence = text[start_index: start_index + SEQ_LENGTH]
            generated += sentence
            for i in range(length):
                x_predictions = np.zeros((1, SEQ_LENGTH, len(characters)))
                for t, char in enumerate(sentence):
                    x_predictions[0, t, char_to_index[char]] = 1

                predictions = model.predict(x_predictions, verbose=0)[0]
                next_index = sample(predictions,
                                        temperature)
                next_character = index_to_char[next_index]

                generated += next_character
                sentence = sentence[1:] + next_character
            return generated
        return generate_text(100, 1)


def stihPolz(x):
        def stih(x):
            xl = ['rodina.txt','love.txt','live.txt','priroda.txt']
            if x in xl:
                text = open(f'{x}', 'rb')\
                    .read().decode(encoding='utf-8').lower()
                # print(text)
                text = text[100:206500]
                # text = text[100:36500]




                characters = sorted(set(text))
                # print(characters)



                char_to_index = dict((c, i) for i, c in enumerate(characters))
                index_to_char = dict((i, c) for i, c in enumerate(characters))

                SEQ_LENGTH = 60
                STEP_SIZE = 3

                sentences = []
                next_char = []

                for i in range(0, len(text) - SEQ_LENGTH, STEP_SIZE):
                    sentences.append(text[i: i + SEQ_LENGTH])
                    next_char.append(text[i + SEQ_LENGTH])

                x = np.zeros((len(sentences), SEQ_LENGTH,
                            len(characters)), dtype=np.bool)
                y = np.zeros((len(sentences),
                            len(characters)), dtype=np.bool)

                for i, satz in enumerate(sentences):
                    for t, char in enumerate(satz):
                        x[i, t, char_to_index[char]] = 1
                    y[i, char_to_index[next_char[i]]] = 1

                model = Sequential()
                model.add(LSTM(128,
                            input_shape=(SEQ_LENGTH,
                                            len(characters))))
                model.add(Dense(len(characters)))
                model.add(Activation('softmax'))

                model.compile(loss='categorical_crossentropy',
                            optimizer=RMSprop(lr=0.01))

                model.fit(x, y, batch_size=256, epochs=6)

                def sample(preds, temperature=1.0):
                    preds = np.asarray(preds).astype('float64')
                    preds = np.log(preds) / temperature
                    exp_preds = np.exp(preds)
                    preds = exp_preds / np.sum(exp_preds)
                    probas = np.random.multinomial(1, preds, 1)
                    return np.argmax(probas)


                def generate_text(length, temperature):
                    start_index = random.randint(0, len(text) - SEQ_LENGTH - 1)
                    generated = ''
                    sentence = text[start_index: start_index + SEQ_LENGTH]
                    generated += sentence
                    for i in range(length):
                        x_predictions = np.zeros((1, SEQ_LENGTH, len(characters)))
                        for t, char in enumerate(sentence):
                            x_predictions[0, t, char_to_index[char]] = 1

                        predictions = model.predict(x_predictions, verbose=0)[0]
                        next_index = sample(predictions,
                                                temperature)
                        next_character = index_to_char[next_index]

                        generated += next_character
                        sentence = sentence[1:] + next_character
                    return generated
                return generate_text(100, 1)
        # stih(x)
        return stih(x)

def stihPolz2():
    for i in range(1):
    

        dt = 'inputPolz.txt'
        text = open(f'{dt}', 'rb')\
            .read().decode(encoding='utf-8').lower()



        # print(text)
        text = text[1:1000]
        # text = text[100:36500]




        characters = sorted(set(text))
        # print(characters)



        char_to_index = dict((c, i) for i, c in enumerate(characters))
        index_to_char = dict((i, c) for i, c in enumerate(characters))

        SEQ_LENGTH = 60
        STEP_SIZE = 3

        sentences = []
        next_char = []

        for i in range(0, len(text) - SEQ_LENGTH, STEP_SIZE):
            sentences.append(text[i: i + SEQ_LENGTH])
            next_char.append(text[i + SEQ_LENGTH])

        x = np.zeros((len(sentences), SEQ_LENGTH,
                    len(characters)), dtype=np.bool)
        y = np.zeros((len(sentences),
                    len(characters)), dtype=np.bool)

        for i, satz in enumerate(sentences):
            for t, char in enumerate(satz):
                x[i, t, char_to_index[char]] = 1
            y[i, char_to_index[next_char[i]]] = 1

        model = Sequential()
        model.add(LSTM(128,
                    input_shape=(SEQ_LENGTH,
                                    len(characters))))
        model.add(Dense(len(characters)))
        model.add(Activation('softmax'))

        model.compile(loss='categorical_crossentropy',
                    optimizer=RMSprop(lr=0.01))

        model.fit(x, y, batch_size=256, epochs=100)

        def sample(preds, temperature=1.0):
            preds = np.asarray(preds).astype('float64')
            preds = np.log(preds) / temperature
            exp_preds = np.exp(preds)
            preds = exp_preds / np.sum(exp_preds)
            probas = np.random.multinomial(1, preds, 1)
            return np.argmax(probas)


        def generate_text(length, temperature):
            start_index = random.randint(0, len(text) - SEQ_LENGTH - 1)
            generated = ''
            sentence = text[start_index: start_index + SEQ_LENGTH]
            generated += sentence
            for i in range(length):
                x_predictions = np.zeros((1, SEQ_LENGTH, len(characters)))
                for t, char in enumerate(sentence):
                    x_predictions[0, t, char_to_index[char]] = 1

                predictions = model.predict(x_predictions, verbose=0)[0]
                next_index = sample(predictions,
                                        temperature)
                next_character = index_to_char[next_index]

                generated += next_character
                sentence = sentence[1:] + next_character
            return generated
        return generate_text(100, 1)
