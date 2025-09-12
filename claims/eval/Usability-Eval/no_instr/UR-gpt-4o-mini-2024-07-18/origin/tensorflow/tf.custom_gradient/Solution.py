import tensorflow as tf

def custom_gradient(func):
    @tf.custom_gradient
    def wrapped(*args, **kwargs):
        # Compute the output using the original function
        output = func(*args, **kwargs)

        # Define the gradient
        def grad(dy):
            # Custom gradient logic here
            return dy * 2  # Example: double the gradient

        return output, grad
    
    return wrapped

# Example usage of the decorator
@custom_gradient
def my_function(x):
    return x ** 2

# Testing the function and custom gradient
with tf.GradientTape() as tape:
    x = tf.Variable(3.0)
    y = my_function(x)

grad = tape.gradient(y, x)
print(f"Function output: {y.numpy()}, Gradient: {grad.numpy()}")
