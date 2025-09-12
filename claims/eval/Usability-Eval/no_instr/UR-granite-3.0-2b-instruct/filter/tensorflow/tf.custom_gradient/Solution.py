import tensorflow as tf

# Define a custom gradient function
def custom_gradient(f):
    def wrapped_f(*args, **kwargs):
        with tf.GradientTape() as tape:
            tape.watch(*args)
            result = f(*args, **kwargs)
        grad = tape.gradient(result, *args)
        return result, grad
    return wrapped_f

# Define a function to be decorated
@custom_gradient
def custom_function(x):
    return x ** 2

# Test the function
x = tf.Variable(3.0)
y, grad = custom_function(x)
print("Function value:", y.numpy())
print("Gradient:", grad.numpy())
