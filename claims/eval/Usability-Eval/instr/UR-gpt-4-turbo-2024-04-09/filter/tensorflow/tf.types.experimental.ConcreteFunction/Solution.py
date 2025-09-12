import tensorflow as tf

class DifferentiableGraphFunction(tf.Module):
    def __init__(self, name=None):
        super().__init__(name=name)

    def call(self, inputs):
        raise NotImplementedError("Subclasses must implement the call method.")
