import tensorflow as tf

class DifferentiableGraphFunction(tf.Module):
    def __init__(self, name=None):
        super(DifferentiableGraphFunction, self).__init__(name=name)
        self.variables = []

    def __call__(self, inputs):
        with tf.GradientTape() as tape:
            tape.watch(inputs)
            outputs = self.forward(inputs)
        gradients = tape.gradient(outputs, inputs)
        return outputs, gradients

    def forward(self, inputs):
        raise NotImplementedError("Subclasses should implement the forward method.")

# Example subclass implementation
class MyGraphFunction(DifferentiableGraphFunction):
    def __init__(self, name=None):
        super(MyGraphFunction, self).__init__(name=name)
        self.weights = tf.Variable(tf.random.normal([inputs.shape[1], 1]), name='weights')
        self.bias = tf.Variable(tf.zeros([1]), name='bias')
        self.variables.extend([self.weights, self.bias])

    def forward(self, inputs):
        return tf.matmul(inputs, self.weights) + self.bias

# Example usage
inputs = tf.constant([[1.0, 2.0], [3.0, 4.0]])
my_graph_function = MyGraphFunction()
outputs, gradients = my_graph_function(inputs)

print("Outputs:", outputs.numpy())
print("Gradients:", gradients.numpy())
