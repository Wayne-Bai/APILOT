import tensorflow as tf
from tensorflow.keras.layers import Dense
from sklearn.base import RegressorMixin

class TensorFlowClassifier(RegressorMixin):
    def __init__(self, hidden_size=100):
        self.hidden_size = hidden_size
        self.model = None

    def fit(self, X, y):
        self.model = tf.keras.Sequential([
            Dense(self.hidden_size, input_shape=(X.shape[1],)),
            Dense(1)
        ])
        self.model.compile(optimizer='adam', loss='mse')
        self.model.fit(X, y, epochs=100, verbose=0)
        return self

    def predict(self, X):
        return self.model.predict(X)
