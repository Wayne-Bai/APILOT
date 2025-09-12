
import tensorflow as tf

@tf.custom_gradient
def custom_gradient_function(x):
    def grad(dy):
        # Define custom gradient calculation here
        return dy

    return x, grad

# Example usage of the custom gradient function
input_value = tf.constant(5.0)
output = custom_gradient_function(input_value)

with tf.GradientTape() as tape:
    tape.watch(input_value)
    result = custom_gradient_function(input_value)

gradient = tape.gradient(result, input_value)

print("Input Value:", input_value.numpy())
print("Output:", result.numpy())
print("Gradient:", gradient.numpy())
