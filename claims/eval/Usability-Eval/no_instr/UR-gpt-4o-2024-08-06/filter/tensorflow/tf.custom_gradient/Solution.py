import tensorflow as tf

# Define the decorator for applying a custom gradient
def custom_gradient_decorator(func):
    @tf.custom_gradient
    def decorated_function(x):
        # The main function behavior
        y = func(x)
        
        # Custom gradient calculation
        def custom_grad(dy):
            # This is the gradient at `x` for the output `y`
            # Custom gradient logic can be added here
            grad = dy * 2.0 * x 
            return grad

        return y, custom_grad

    return decorated_function

# Example usage
@custom_gradient_decorator
def my_square(x):
    return x ** 2

# Example with gradient calculation
x = tf.constant(3.0)
with tf.GradientTape() as tape:
    tape.watch(x)
    y = my_square(x)

# Compute the gradient
dy_dx = tape.gradient(y, x)
print(f'dy/dx: {dy_dx.numpy()}')  # Output will depend on the custom gradient logic defined
