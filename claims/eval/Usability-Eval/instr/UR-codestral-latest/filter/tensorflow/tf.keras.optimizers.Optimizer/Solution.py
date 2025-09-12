import tensorflow as tf

class Optimizer(tf.keras.optimizers.Optimizer):
    def __init__(self, name, **kwargs):
        super(Optimizer, self).__init__(name, **kwargs)

    def get_updates(self, loss, params):
        raise NotImplementedError('Must be implemented in subclass.')

    def apply_gradients(self, grads_and_vars, name=None, experimental_aggregate_gradients=True):
        raise NotImplementedError('Must be implemented in subclass.')
