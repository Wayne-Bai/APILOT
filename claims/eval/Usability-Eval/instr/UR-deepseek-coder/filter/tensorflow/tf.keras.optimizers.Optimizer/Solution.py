import tensorflow as tf

class AbstractOptimizer(tf.Module):
    def __init__(self, learning_rate=0.01, name="AbstractOptimizer"):
        super(AbstractOptimizer, self).__init__(name=name)
        self.learning_rate = tf.Variable(learning_rate, trainable=False, name="learning_rate")

    def apply_gradients(self, grads_and_vars):
        raise NotImplementedError("Subclasses should implement this method")

    def minimize(self, loss, var_list):
        grads_and_vars = self.compute_gradients(loss, var_list)
        self.apply_gradients(grads_and_vars)

    def compute_gradients(self, loss, var_list):
        grads = tf.gradients(loss, var_list)
        return list(zip(grads, var_list))
