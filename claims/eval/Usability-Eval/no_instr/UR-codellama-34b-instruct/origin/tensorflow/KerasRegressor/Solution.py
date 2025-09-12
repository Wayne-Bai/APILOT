import numpy as np
from sklearn.base import RegressorMixin
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, InputLayer
from tensorflow.keras.utils import to_categorical

class TensorFlowRegressor(RegressorMixin):
    def __init__(self, model, input_shape=None, output_shape=None, **kwargs):
        self.model = model
        self.input_shape = input_shape
        self.output_shape = output_shape
        super().__init__(**kwargs)
        
    def fit(self, X, y):
        if self.input_shape is None:
            self.input_shape = X.shape[1:]
        if self.output_shape is None:
            self.output_shape = np.atleast_2d(y).shape[1:]
            
        X_input = InputLayer(self.input_shape)
        X_dense = Dense(units=32, activation='relu')(X_input)
        X_dropout = Dropout(rate=0.5)(X_dense)
        X_output = Dense(units=self.output_shape[1], activation='sigmoid')(X_dropout)
        
        self.model = Sequential()
        self.model.add(X_input)
        self.model.add(X_dense)
        self.model.add(X_dropout)
        self.model.add(X_output)
        
        self.model.compile(loss='mean_squared_error', optimizer='adam')
        self.model.fit(X, y, epochs=100, verbose=0)
        
    def predict(self, X):
        return self.model.predict(X)
