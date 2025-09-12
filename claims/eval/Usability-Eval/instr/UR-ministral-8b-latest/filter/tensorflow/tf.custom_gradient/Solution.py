import tensorflow as tf

class CustomGradient:
    def __init__(self, grad_fn):
        self.grad_fn = grad_fn

    def __call__(self, func):
        def wrapped(*args, **kwargs):
            grad = self.grad_fn(func, *args, **kwargs)
            return grad
        return wrapped

@CustomGradient(grad_fn=lambda func, *args, **kwargs: tf.gradients(func, *args, **kwargs))
def custom_gradient_function(x):
    return x * 2

x = tf.Variable(0.0, name='x')
result = custom_gradient_function(x)

with tf.GradientTape() as tape:
    tape.watch(x)
    y = custom_gradient_function(x)
    d_minmax_gradient = tape.gradient(y, x)

print(f'Gradient: {d_minmax_gradient}')
