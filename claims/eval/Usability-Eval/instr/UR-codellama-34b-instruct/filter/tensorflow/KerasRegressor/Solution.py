import tensorflow as tf
from tensorflow import keras
from sklearn.base import RegressorMixin

class TensorFlowRegressor(keras.Model, RegressorMixin):
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model

    def fit(self, X, y=None, epochs=100, verbose=True, callbacks=None, validation_split=0.2, shuffle=True):
        return self.model.fit(X, y, epochs=epochs, verbose=verbose, callbacks=callbacks, validation_split=validation_split, shuffle=shuffle)

    def predict(self, X):
        return self.model.predict(X)
