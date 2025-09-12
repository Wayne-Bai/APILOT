import tensorflow as tf

@tf.custom_gradient
def custom_grad_func(x):
    def grad(dy):
        return dy * 2  # This is the custom gradient function

    return x * 2  # This is the main function

# Create a tensor
x = tf.Variable(3.0)

# Compute the output
y = custom_grad_func(x)

# Print the output
print(y.numpy())  # Output: 6.0

# Compute the gradient
dy = tf.constant(1.0)
grad_value = tf.custom_gradient(custom_grad_func, x)[1](dy)
print(grad_value.numpy())  # Output: 2.0
