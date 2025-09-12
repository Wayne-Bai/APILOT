# Importing necessary libraries
import tensorflow as tf
from abc import ABC, abstractmethod

# Base class for polymorphic graph functions
class GraphFunction(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def build_graph(self):
        pass

    def __call__(self, inputs):
        return self.build_graph()(inputs)

# Example usage: Defining a Simple Graph Function
class SimpleGraphFunction(GraphFunction):
    def __init__(self, name):
        super().__init__(name)

    def build_graph(self):
        return tf.function(lambda x: tf.square(x))

# Creating an instance of SimpleGraphFunction
simple_graph = SimpleGraphFunction("SimpleGraph")

# Testing the SimpleGraphFunction
inputs = tf.constant([1.0, 2.0, 3.0])
print(simple_graph(inputs))

# Example usage: Defining a Dense Graph Function
class DenseGraphFunction(GraphFunction):
    def __init__(self, units, name):
        super().__init__(name)
        self.units = units

    def build_graph(self):
        return tf.function(lambda x: tf.keras.layers.Dense(self.units)(x))

# Creating an instance of DenseGraphFunction
dense_graph = DenseGraphFunction(32, "DenseGraph")

# Testing the DenseGraphFunction
inputs = tf.keras.Input(shape=(10,))
print(dense_graph(inputs))
