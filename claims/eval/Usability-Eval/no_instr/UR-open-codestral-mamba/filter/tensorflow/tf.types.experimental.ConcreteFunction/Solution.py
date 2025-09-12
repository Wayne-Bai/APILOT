import tensorflow as tf

class DifferentiableGraphFunction(tf.Module):
    def __init__(self, name=None):
        super().__init__(name=name)

    @tf.function
    def grad(self, x):
        with tf.GradientTape() as t:
            t.watch(x)
            y = self.__call__(x)
        return t.gradient(y, x)
