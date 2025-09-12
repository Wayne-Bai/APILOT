import tensorflow as tf
import numpy as np

# Define a simple neural network model
x = tf.Variable([1.0])

def custom_gradient(model):
    """
    Define a custom gradient for the model.
    
    Args:
    model: tf.Operation or tf.Tensor, the model to apply the custom gradient to.
    
    Returns:
    tf.Operation, the graph operation representing the custom gradient.
    """
    with tf.GradientTape() as tape:
        tape.watch(model)
        return tape.gradient(model, model)

@tf.custom_gradient
def sigmoid(x):
    """
    A sigmoid function with a custom gradient.
    
    Args:
    x (tf.Tensor), the input to the sigmoid function.
    
    Returns:
    tf.Tensor, the output of the sigmoid function.
    """
    y = 1 / (1 + tf.exp(-x))
    def grad(dy):
        return dy * y * (1 - y)
    return y, grad

# Use the sigmoid function with a custom gradient
model = tf.sigmoid(x)
grad = custom_gradient(model)

# Compute the gradient using the custom gradient
with tf.GradientTape() as tape:
    tape.watch(x)
    model_value = tf.sigmoid(x)
    loss = tf.square(model_value - 1.0)  # loss function
    gradient = tape.gradient(loss, x)

# Print the result
print(f"Gradient of the model: {grad(x).numpy()}")
print(f"Gradient of the loss: {gradient.numpy().flatten()}")

