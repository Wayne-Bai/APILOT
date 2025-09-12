import tensorflow as tf

class AbstractOptimizer(tf.Module):
    def __init__(self, learning_rate):
        super().__init__()
        self.learning_rate = learning_rate

    def apply_gradients(self, grads_and_vars):
        raise NotImplementedError("apply_gradients method needs to be implemented")

    def minimize(self, loss_fn, var_list):
        with tf.GradientTape() as tape:
            loss = loss_fn()
            grads = tape.gradient(loss, var_list)
        self.apply_gradients(zip(grads, var_list))
        return loss
