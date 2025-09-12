import tensorflow as tf

class AbstractOptimizer(tf.keras.optimizers.Optimizer):
    def __init__(self, name="AbstractOptimizer", **kwargs):
        super(AbstractOptimizer, self).__init__(name, **kwargs)

    def _create_slots(self, var_list):
        for var in var_list:
            self.add_slot(var, "momentum")

    def _resource_apply_dense(self, grad, var, apply_state=None):
        raise NotImplementedError("Subclasses must implement this method.")

    def _resource_apply_sparse(self, grad, var, indices, apply_state=None):
        raise NotImplementedError("Subclasses must implement this method.")

    def get_config(self):
        config = super(AbstractOptimizer, self).get_config()
        return config
