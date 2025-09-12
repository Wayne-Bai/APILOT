import tensorflow as tf

def custom_gradient_decorator(gradient_function):
    """Decorator to define a function with a custom gradient.

    Args:
        gradient_function: This is the function that computes the custom gradient.

    Returns:
        A Python function that acts as a decorator.
    """
    def decorator(func):
        @tf.custom_gradient
        def wrapper(*args, **kwargs):
            def grad(dy):
                return gradient_function(dy, *args, **kwargs)
            return func(*args, **kwargs), grad
        return wrapper
    return decorator

# Example usage
@custom_gradient_decorator(gradient_function=lambda dy, x: dy * 2 * x)
def square(x):
    return x**2

# Test the custom gradient
x = tf.constant(3.0)
with tf.GradientTape() as tape:
    tape.watch(x)
    y = square(x)
dy_dx = tape.gradient(y, x)  # Should compute to 2*x, which is 6.0 for x=3.0

print("y:", y.numpy())  # Should print 9.0, as square(3) = 3^2
print("dy_dx:", dy_dx.numpy())  # Should print 6.0, as 2*3 = 6
