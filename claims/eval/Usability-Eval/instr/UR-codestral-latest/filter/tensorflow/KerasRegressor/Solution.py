import tensorflow as tf
from sklearn.base import RegressorMixin, BaseEstimator

class TensorFlowRegressor(BaseEstimator, RegressorMixin):
    def __init__(self, epochs=100, batch_size=32, learning_rate=0.01):
        self.epochs = epochs
        self.batch_size = batch_size
        self.learning_rate = learning_rate

    def fit(self, X, y):
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(32, activation='relu', input_shape=[X.shape[1]]),
            tf.keras.layers.Dense(1)
        ])

        optimizer = tf.keras.optimizers.Adam(learning_rate=self.learning_rate)
        self.model.compile(loss='mse', optimizer=optimizer, metrics=['mae'])
        self.model.fit(X, y, epochs=self.epochs, batch_size=self.batch_size)

    def predict(self, X):
        return self.model.predict(X)
