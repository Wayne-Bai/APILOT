import tensorflow as tf

class DifferentiableGraphFunction(tf.Module):
    def __init__(self):
        super(DifferentiableGraphFunction, self).__init__()
        self.variables = []

    def forward(self, *inputs):
        raise NotImplementedError("The forward method must be implemented by subclasses.")

    def add_variable(self, name, shape, initializer=tf.initializers.GlorotUniform()):
        variable = tf.Variable(initializer(shape=shape), name=name)
        self.variables.append(variable)
        return variable

    @tf.function
    def compute_gradient(self, inputs, target):
        with tf.GradientTape() as tape:
            tape.watch(self.variables)
            prediction = self.forward(*inputs)
            loss = self.loss_function(prediction, target)
        gradients = tape.gradient(loss, self.variables)
        return gradients

    def loss_function(self, prediction, target):
        return tf.reduce_mean(tf.square(prediction - target))

# Example subclass implementing a specific graph function
class LinearModel(DifferentiableGraphFunction):
    def __init__(self, input_dim, output_dim):
        super(LinearModel, self).__init__()
        self.weights = self.add_variable("weights", shape=[input_dim, output_dim])
        self.bias = self.add_variable("bias", shape=[output_dim])

    def forward(self, inputs):
        return tf.matmul(inputs, self.weights) + self.bias
