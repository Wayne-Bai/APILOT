import tensorflow as tf

class AbstractOptimizer:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    def compute_gradients(self, loss, params):
        raise NotImplementedError

    def apply_gradients(self, grads_and_vars):
        raise NotImplementedError

    def optimize(self, loss, params):
        grads = self.compute_gradients(loss, params)
        self.apply_gradients(grads)

class MyOptimizer(AbstractOptimizer):
    def compute_gradients(self, loss, params):
        with tf.GradientTape() as tape:
            loss_value = loss(params)
        grads = tape.gradient(loss_value, params)
        return grads

    def apply_gradients(self, grads_and_vars):
        for grad, var in grads_and_vars:
            var.assign_add(grad)

    def optimize(self, loss, params):
        grads = self.compute_gradients(loss, params)
        self.apply_gradients(grads)
