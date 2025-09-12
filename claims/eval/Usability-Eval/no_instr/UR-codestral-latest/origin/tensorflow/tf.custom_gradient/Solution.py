import tensorflow as tf

def custom_gradient(f):
    @tf.custom_gradient
    def grad(x):
        result = f(x)
        def custom_grad(dy):
            # Define your custom gradient computation here
            return dy * 2 * x
        return result, custom_grad
    return grad
