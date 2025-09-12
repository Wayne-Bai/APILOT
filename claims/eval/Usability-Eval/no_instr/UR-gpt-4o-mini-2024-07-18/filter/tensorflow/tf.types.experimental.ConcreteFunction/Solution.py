import tensorflow as tf

class DifferentiableGraphFunction(tf.Module):
    def __init__(self):
        super(DifferentiableGraphFunction, self).__init__()

    def call(self, inputs):
        raise NotImplementedError("Subclasses should implement this method.")

    def compute_gradients(self, inputs):
        with tf.GradientTape() as tape:
            tape.watch(inputs)
            output = self.call(inputs)
        gradients = tape.gradient(output, inputs)
        return output, gradients

# Example subclass implementation
class MyGraphFunction(DifferentiableGraphFunction):
    def call(self, inputs):
        return tf.reduce_sum(inputs ** 2)

# Usage
graph_function = MyGraphFunction()
inputs = tf.constant([1.0, 2.0, 3.0])
output, gradients = graph_function.compute_gradients(inputs)

print("Output:", output.numpy())
print("Gradients:", gradients.numpy())
