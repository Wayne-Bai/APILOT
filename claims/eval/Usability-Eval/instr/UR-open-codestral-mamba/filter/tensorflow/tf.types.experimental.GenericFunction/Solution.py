import tensorflow as tf

class PolymorphicGraph(object):
    def __init__(self, input_shape):
        self.input_shape = input_shape
        self.inputs = tf.placeholder(tf.float32, shape=input_shape)
        self.outputs = self.build_graph(self.inputs)

    def build_graph(self, inputs):
        # This method should be overridden by derived classes
        raise NotImplementedError
