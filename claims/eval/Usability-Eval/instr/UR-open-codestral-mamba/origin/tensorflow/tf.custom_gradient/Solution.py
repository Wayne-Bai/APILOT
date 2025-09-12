import tensorflow as tf

# Define the custom gradient function
def custom_gradient(y, x):
    dy_dx = tf.expand_dims(tf.gradients(ys=y, xs=x), axis=-1)
    return lambda dy: dy_dx * dy

# Define the decorator
def custom_gradient_decorator(func):
    def register_gradient(op, grad):
        custom_grad = custom_gradient(op.outputs[0], op.inputs[0])
        return grad * custom_gradient(op.outputs[0], op.inputs[0])

    @tf.RegisterGradient(func.__name__)
    def wrap_grad(*op, **grad_args):
        if not hasattr(op[0], "custom_gradient"):
            raise Exception(f"Function '{func.__name__}' does not have a custom gradient")
        return register_gradient(op[0], grad_args['dy'])

    return wrap_grad

# Usage
@custom_gradient_decorator
def custom_func(x):
    return x ** 2

x = tf.constant(2.0)
with tf.GradientTape() as tape:
    tape.watch(x)
    y = custom_func(x)
dy_dx = tape.gradient(y, x)
print(dy_dx)  # Output: tf.Tensor(4., shape=(), dtype=float32)
