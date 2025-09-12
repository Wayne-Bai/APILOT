import tensorflow as tf

def custom_gradient(func):
    def decorated_func(*args, **kwargs):
        x = tf.Variable(0.0)
        with tf.GradientTape() as tape:
            tape.watch(x)
            y = func(*args, **kwargs)
        grad = tape.gradient(y, x)
        return y, grad
    return decorated_func

@custom_gradient
def example_function(x):
    return x ** 2

x = tf.Variable(2.0)
y, grad = example_function(x)
print(f"Output: {y}, Gradient: {grad}")
