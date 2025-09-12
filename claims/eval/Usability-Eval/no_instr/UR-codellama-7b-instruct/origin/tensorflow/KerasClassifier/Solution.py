
import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import Sequential

class TensorFlowClassifier(tf.keras.Model):
    def __init__(self, num_classes):
        super().__init__()
        self.dense1 = Dense(64, activation='relu')
        self.dense2 = Dense(num_classes)

    def call(self, inputs):
        x = self.dense1(inputs)
        return self.dense2(x)
