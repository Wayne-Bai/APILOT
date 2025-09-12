import tensorflow as tf

def custom_gradient_function(func):
    @tf.custom_gradient
    def wrapper(*args, **kwargs):
        y = func(*args, **kwargs)

        def grad(*dy):
            with tf.GradientTape() as tape:
                tape.watch(args)
                y = func(*args, **kwargs)
            return tape.gradient(y, args, output_gradients=dy)

        return y, grad
    return wrapper

@custom_gradient_function
def my_function(x):
    return x ** 2

# Example usage
x = tf.Variable(3.0)
with tf.GradientTape() as tape:
    y = my_function(x)
grad = tape.gradient(y, x)

print("Function output:", y.numpy())
print("Gradient:", grad.numpy())
