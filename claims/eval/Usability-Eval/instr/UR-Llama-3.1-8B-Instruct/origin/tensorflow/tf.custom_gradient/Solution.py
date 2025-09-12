import tensorflow as tf
from tensorflow.python.framework import ops, autograph

# Define a decorator to define a function with a custom gradient
def func_grad(func):
    @tf.RegisterGradient(func)
    def grad(op, grad_output):
        x, y = op.inputs
        return op.inputs, func(y, grad_output)  # Add gradients of x and y
    return func

# Define a custom gradient function
@func_grad
def my_func(x, y):
    return x * y

# Create a computational graph
with tf.Session() as sess:
    # Initialize placeholders for input and output
    tf.enable_eager_execution()
    x = 2.0
    y = 3.0
    
    # Compute output using my_func
    output = my_func(x, y)
    
    # Compute gradients of x and y with respect to output
    grads = tf.gradients(output, [x, y])
    
    # Print the output and gradients
    print("Output:", output)
    print("Gradients: ", grads)

