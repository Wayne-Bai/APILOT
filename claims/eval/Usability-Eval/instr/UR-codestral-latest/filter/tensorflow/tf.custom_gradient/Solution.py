import tensorflow as tf

def custom_gradient(f):
    @tf.custom_gradient
    def g(x, *args, **kwargs):
        y = f(x, *args, **kwargs)
        def grad(dy):
            # Here you can modify the gradient as required
            # By default it uses standard gradient computation, but you could either
            # multiply or divide dy by a value, or compute a different gradient.
            return dy
        return y, grad
    return g

@custom_gradient
def f1(x):
    return tf.square(x)

# Test the function
with tf.GradientTape() as g:
    x = tf.Variable(2.0)
    y = f1(x)

# Old TensorFlow listed API was changed in TensorFlow 2.0, thus there
# is no longer a need to use tf.gradients to compute gradients.
grad_y = g.gradient(y, x)
print(grad_y)
