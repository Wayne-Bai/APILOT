import tensorflow as tf

class DifferentiableGraphFunction(tf.Module):
    def __init__(self, input_shape, output_shape):
        super(DifferentiableGraphFunction, self).__init__(name='differentiable_graph_function')
        self.input_shape = input_shape
        self.output_shape = output_shape

    def call(self, inputs):
        # Implement the forward pass of your differentiable graph function here
        raise NotImplementedError('You must implement the `call` method in a subclass')

    def gradients(self, inputs):
        # Implement the gradient computation of your differentiable graph function here
        raise NotImplementedError('You must implement the `gradients` method in a subclass')
