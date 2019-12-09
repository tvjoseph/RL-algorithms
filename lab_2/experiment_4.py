from dqn_agent import DQNAgent, perform_experiment
import gym
import numpy as np
from keras.layers import Dense, Dropout
from keras.optimizers import Adam
from keras.models import Sequential, model_from_json


def get_model_1(input_size, output_size, lr):
    model = Sequential()
    model.add(Dense(4, input_dim=input_size, activation='relu',
                    kernel_initializer='he_uniform'))
    model.add(Dense(output_size, activation='linear',
                    kernel_initializer='he_uniform'))
    model.compile(loss='mse', optimizer=Adam(lr=lr))
    return model

def get_model_2(input_size, output_size, lr):
    model = Sequential()
    model.add(Dense(16, input_dim=input_size, activation='relu',
                    kernel_initializer='he_uniform'))
    model.add(Dense(output_size, activation='linear',
                    kernel_initializer='he_uniform'))
    model.compile(loss='mse', optimizer=Adam(lr=lr))
    return model

def get_model_3(input_size, output_size, lr):
    model = Sequential()
    model.add(Dense(64, input_dim=input_size, activation='relu',
                    kernel_initializer='he_uniform'))
    model.add(Dense(output_size, activation='linear',
                    kernel_initializer='he_uniform'))
    model.compile(loss='mse', optimizer=Adam(lr=lr))
    return model

def get_model_4(input_size, output_size, lr):
    model = Sequential()
    model.add(Dense(8, input_dim=input_size, activation='relu',
                    kernel_initializer='he_uniform'))
    model.add(Dense(16, input_dim=input_size, activation='relu',
                    kernel_initializer='he_uniform'))
    model.add(Dense(output_size, activation='linear',
                    kernel_initializer='he_uniform'))
    model.compile(loss='mse', optimizer=Adam(lr=lr))
    return model

def get_model_5(input_size, output_size, lr):
    model = Sequential()
    model.add(Dense(8, input_dim=input_size, activation='relu',
                    kernel_initializer='he_uniform'))
    model.add(Dense(16, input_dim=input_size, activation='relu',
                    kernel_initializer='he_uniform'))
    model.add(Dense(8, input_dim=input_size, activation='relu',
                    kernel_initializer='he_uniform'))
    model.add(Dense(output_size, activation='linear',
                    kernel_initializer='he_uniform'))
    model.compile(loss='mse', optimizer=Adam(lr=lr))
    return model


if __name__ == "__main__":
    models = [get_model_1, get_model_2, get_model_3]
    discount_factors = [0.95]
    learning_rates = [0.001]
    memory_sizes = [10000]
    update_frequencies = [5]

    perform_experiment(models = models,
                        discount_factors = discount_factors,
                        learning_rates = learning_rates,
                        memory_sizes = memory_sizes,
                        update_frequencies = update_frequencies)