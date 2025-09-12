import tensorflow as tf
from sklearn.base import RegressorMixin

class TensorFlowRegressor(RegressorMixin):
    def __init__(self):
        self.model = tf.keras.Sequential()

    def fit(self, X, y):
        self.model.add(tf.keras.layers.Dense(64, input_dim=X.shape[1]))
        self.model.add(tf.keras.layers.Activation('relu'))
        self.model.add(tf.keras.layers.Dense(1))
        self.model.compile(optimizer='adam', loss='mse', metrics=['accuracy'])
        self.model.fit(X, y, epochs=100, batch_size=32)

    def predict(self, X):
        return self.model.predict(X)
