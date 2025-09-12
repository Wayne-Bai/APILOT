import tensorflow as tf
from sklearn.base import RegressorMixin, BaseEstimator
import numpy as np

class TFRegressor(BaseEstimator, RegressorMixin):
    def __init__(self, input_shape, output_shape, epochs=100, batch_size=32, learning_rate=0.001):
        self.input_shape = input_shape
        self.output_shape = output_shape
        self.epochs = epochs
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.model = self._build_model()

    def _build_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.InputLayer(input_shape=(self.input_shape,)),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(self.output_shape)
        ])
        optimizer = tf.keras.optimizers.Adam(learning_rate=self.learning_rate)
        model.compile(optimizer=optimizer, loss='mse', metrics=['mae'])
        return model

    def fit(self, X, y):
        self.model.fit(X, y, epochs=self.epochs, batch_size=self.batch_size, verbose=0)

    def predict(self, X):
        return self.model.predict(X)
    
    def score(self, X, y):
        predictions = self.predict(X)
        return np.mean(np.square(predictions - y))
