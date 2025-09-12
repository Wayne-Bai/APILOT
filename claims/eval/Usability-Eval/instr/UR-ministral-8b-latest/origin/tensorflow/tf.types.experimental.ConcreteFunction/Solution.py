import tensorflow as tf

class BaseDifferentiableFunction:
    """
    A base class for differentiable graph functions.
    """

    def __call__(self, *args, **kwargs):
        raise NotImplementedError("Subclasses should implement this to return a callable.")

    def gradient(self, x):
        raise NotImplementedError("Subclasses should implement this to return a gradient function.")

    def forward(self, x):
        raise NotImplementedError("Subclasses should implement this to return the forward pass.")

class SimpleFunction(BaseDifferentiableFunction):
    def __init__(self, input_dim):
        self.input_dim = input_dim

    def __call__(self, x):
        return tf.reduce_sum(x**2)

    def gradient(self, x):
        def gradient_fn(x):
            return 2 * x
        return tf.function(gradient_fn)

    def forward(self, x):
        return tf.reduce_sum(x**2)

# Example usage
if __name__ == "__main__":
    func = SimpleFunction(3)  # Assuming input has dimension 3
    optimizable_x = tf.Variable(tf.random.normal([3]))

    with tf.GradientTape() as tape:
        tape.watch(optimizable_x)
        loss = func(optimizable_x)

    grads = tape.gradient(loss, optimizable_x)
    print("Gradients:", grads.numpy())
