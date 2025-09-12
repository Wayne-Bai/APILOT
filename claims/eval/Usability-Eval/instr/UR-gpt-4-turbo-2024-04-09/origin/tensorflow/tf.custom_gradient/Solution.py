import tensorflow as tf

def my_custom_gradient(func):
    @tf.custom_gradient
    def wrapper(*args, **kwargs):
        def grad(dy):
            return dy  # Here you can modify gradient calculation manually
        result = func(*args, **kwargs)
        return result, grad
    return wrapper

@my_custom_gradient
def my_function(x):
    return x ** 2  # Example function

# Example usage
x = tf.constant(3.0)
with tf.GradientTape() as tape:
    tape.watch(x)
    y = my_function(x)
dy_dx = tape.gradient(y, x)  # Compute the gradient
print("The gradient is:", dy_dx.numpy())
