import tensorflow as tf

def custom_gradient(f):
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)

    def gradient(dy):
        # Define your custom gradient logic here
        # For example, let's say we want to add 1 to the gradient
        return dy + 1

    grad = tf.GradientTape().gradient(decorated_function, f.variables)
    return grad, gradient

@custom_gradient
def my_function(x):
    return x ** 2

# Test the function
x = tf.Variable(3.0)
with tf.GradientTape() as tape:
    y = my_function(x)
gradient = tape.gradient(y, x)
print(gradient)
