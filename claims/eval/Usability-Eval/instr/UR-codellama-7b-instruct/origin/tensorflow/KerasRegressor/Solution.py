import tensorflow as tf
from tensorflow import keras
from sklearn.base import RegressorMixin, ClassifierMixin

class TFRegressor(keras.Model):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layers = []
    
    def add_layer(self, layer):
        self.layers.append(layer)
    
    def call(self, inputs):
        for layer in self.layers:
            inputs = layer(inputs)
        return inputs
