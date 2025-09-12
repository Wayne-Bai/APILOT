import tensorflow as tf

class DifferentiableGraphFunction(tf.Module):
    def __init__(self, name=None):
        super(DifferentiableGraphFunction, self).__init__(name=name)
    
    def build(self, input_shape):
        # Initialize the model's weights and biases here
        # This example is generic. Replace with relevant code.
        self.weights = tf.Variable(tf.random.normal(input_shape), name='weights')
        self.bias = tf.Variable(tf.zeros([1]), name='bias')
    
    def call(self, inputs):
        # Define the forward computation of the graph function here.
        # This example is generic. Replace with relevant code.
        return tf.add(tf.matmul(inputs, self.weights), self.bias)

    def compute_output_shape(self, input_shape):
        # Here, compute and return the output shape based on the input shape
        # This example simply maintains the input dimensions except the last
        output_shape = input_shape[:-1] + (self.weights.shape[-1],)
        return output_shape
