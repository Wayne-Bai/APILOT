
import tensorflow as tf

class AbstractOptimizer(tf.Module):
    def __init__(self):
        super(AbstractOptimizer, self).__init__()

    def minimize(self, loss, var_list):
        raise NotImplementedError("minimize() method must be implemented in subclass")
