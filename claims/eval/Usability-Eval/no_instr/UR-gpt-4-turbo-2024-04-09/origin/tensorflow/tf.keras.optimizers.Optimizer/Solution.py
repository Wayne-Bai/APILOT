import tensorflow as tf

class MyOptimizer(tf.keras.optimizers.Optimizer):
    def __init__(self, learning_rate=0.01, name="MyOptimizer"):
        super(MyOptimizer, self).__init__(name=name)
        self.learning_rate = learning_rate

    def _create_slots(self, var_list):
        # Create optimizer slots for variables if necessary.
        pass

    def _resource_apply_dense(self, grad, var, apply_state=None):
        # Update the variable given the gradient for dense tensors
        var.assign_sub(grad * self.learning_rate)

    def _resource_apply_sparse(self, grad, var, indices, apply_state=None):
        # Update the variable given the gradient for sparse tensors
        var.scatter_sub(tf.IndexedSlices(grad, indices) * self.learning_rate)

    def get_config(self):
        # Returns the config of the optimizer.
        return {"learning_rate": self.learning_rate}
