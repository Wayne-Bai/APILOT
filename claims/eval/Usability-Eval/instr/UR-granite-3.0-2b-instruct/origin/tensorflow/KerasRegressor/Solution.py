import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.base import RegressorMixin

class TensorFlowRegressor(RegressorMixin, Sequential):
    def __init__(self, units=10, dtype=tf.float32):
        super().__init__()
        self.add(Dense(units, activation='relu', input_shape=(1,), dtype=dtype))
        self.add(Dense(1, activation='linear', dtype=dtype))

    def fit(self, X, y, **kwargs):
        super().fit(X, y, **kwargs)

    def predict(self, X):
        return super().predict(X).numpy().astype(float)
