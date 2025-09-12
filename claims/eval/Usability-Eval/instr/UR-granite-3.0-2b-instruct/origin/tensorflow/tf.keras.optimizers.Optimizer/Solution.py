import tensorflow as tf

class AbstractOptimizer(tf.keras.optimizers.Optimizer):
    def __init__(self, learning_rate=0.001, **kwargs):
        super(AbstractOptimizer, self).__init__(**kwargs)
        self.learning_rate = learning_rate

    def step(self, step):
        raise NotImplementedError

    def apply_gradients(self, gradients, variables):
        with tf.control_dependencies([self.step(step)]):
            return super(AbstractOptimizer, self).apply_gradients(gradients, variables)
