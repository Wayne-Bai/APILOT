
import tensorflow as tf

@tf.RegisterGradient("CustomGrad")
def _custom_grad(unused_op, grad):
    return grad * tf.cast(grad > 0, tf.float32)

@tf.custom_gradient
def custom_func(x):
    def custom_grad(dy):
        return dy * tf.cast(dy > 0, tf.float32)
    
    return x*x, custom_grad

x = tf.constant(2.0)
with tf.GradientTape() as tape:
    tape.watch(x)
    y = custom_func(x)

dy_dx = tape.gradient(y, x)
print(dy_dx)
