import tensorflow as tf

class AbstractOptimizer(tf.keras.optimizers.Optimizer):
    def __init__(self, name, **kwargs):
        super(AbstractOptimizer, self).__init__(name, **kwargs)

    def _resource_apply_dense(self, grad, var, apply_state=None):
        raise NotImplementedError("This method must be implemented in a subclass.")

    def _resource_apply_sparse(self, grad, var, indices, apply_state=None):
        raise NotImplementedError("This method must be implemented in a subclass.")

    def get_config(self):
        base_config = super(AbstractOptimizer, self).get_config()
        return {**base_config}
