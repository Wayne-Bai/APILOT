import tensorflow as tf

# Define the decorator for the custom gradient
def custom_gradient_decorator(fn):
    def wrapped(*args, **kwargs):
        value, grad_fn = fn(*args, **kwargs)

        # Use tf.custom_gradient to define the custom gradient
        @tf.custom_gradient
        def custom_fn(*args):
            def grad(dy):
                return grad_fn(*args, dy)
            return value, grad

        return custom_fn(*args)
    return wrapped

# Example usage
@custom_gradient_decorator
def my_function(x):
    value = x ** 3

    # Define the custom gradient
    def grad_fn(x, dy):
        return dy * 3 * x**2

    return value, grad_fn

# Now, let's test the function and its gradient
x = tf.constant(2.0)
with tf.GradientTape() as tape:
    tape.watch(x)
    y = my_function(x)

# Compute the gradient
dy_dx = tape.gradient(y, x)

print("Function value (y):", y.numpy())
print("Gradient (dy/dx):", dy_dx.numpy())
