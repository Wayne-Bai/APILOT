
import tensorflow as tf

class AbstractOptimizer(object):
    def __init__(self, learning_rate=0.001):
        self.learning_rate = learning_rate

    def apply_gradients(self, grads_and_vars):
        raise NotImplementedError()

    def minimize(self, loss, var_list=None):
        grads_and_vars = self.compute_gradients(loss, var_list)
        return self.apply_gradients(grads_and_vars)

    def compute_gradients(self, loss, var_list=None):
        raise NotImplementedError()
