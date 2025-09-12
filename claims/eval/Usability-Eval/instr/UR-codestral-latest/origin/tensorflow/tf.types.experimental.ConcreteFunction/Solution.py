import tensorflow as tf

class DifferentiableGraphFunction(tf.keras.Model):
    def __init__(self):
        super(DifferentiableGraphFunction, self).__init__()
        # Here you can define your layers or initialize variables that
        # your custom function will use.

    def call(self, inputs):
        # Implement a differentiable function here. This method should
        # return a tf.Tensor which is derived from the 'inputs' tensor.
        # You can use built-in operations from TensorFlow for that, for example:
        # result = tf.sin(inputs)

        # For this basic example, I'll just return the input as is.
        result = inputs

        return result

# Instantiate the model
model = DifferentiableGraphFunction()

# You can use the model to perform computations or calculate gradients.
# For example, with 'tf.GradientTape()' you can calculate the gradient of the
# output with respect to the input.
input_tensor = tf.Variable(2.0)
with tf.GradientTape() as tape:
    output_tensor = model(input_tensor)
gradients = tape.gradient(output_tensor, input_tensor)

print(f'Output tensor: {output_tensor}')
print(f'Gradients: {gradients}')
