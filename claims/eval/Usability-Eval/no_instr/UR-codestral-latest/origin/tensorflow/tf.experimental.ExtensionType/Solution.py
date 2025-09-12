import tensorflow as tf
from tensorflow.python.framework import ops
from tensorflow.python.framework import dtypes

class TensorFlowExtended(tf.Module):
    def __init__(self, name=None):
        super(TensorFlowExtended, self).__init__(name=name)

    # Define your methods here
    # E.g., a method for custom layer creation
    def create_layer(self, input_size, output_size, activation=None):
        self.W = self.add_weight(shape=(input_size, output_size),
                                 initializer="random_normal",
                                 trainable=True)

        self.b = self.add_weight(shape=(output_size,),
                                 initializer="zeros",
                                 trainable=True)

        if activation:
            return activation(tf.matmul(input_size, self.W) + self.b)
        return tf.matmul(input_size, self.W) + self.b
