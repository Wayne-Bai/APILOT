import tensorflow as tf

class AbstractOptimizer(tf.keras.optimizers.Optimizer):
    def __init__(self, name="AbstractOptimizer", **kwargs):
        super(AbstractOptimizer, self).__init__(name, **kwargs)

    def _create_slots(self, var_list):
        # Create a slot for each variable
        for var in var_list:
            self.add_slot(var, 'momentum')

    def _resource_apply_dense(self, grad, var, apply_state=None, name=None):
        raise NotImplementedError("Must be implemented in subclasses.")

    def _resource_apply_sparse(self, grad, var, indices, apply_state=None, name=None):
        raise NotImplementedError("Must be implemented in subclasses.")

    def _lookup_slot(self, var, name):
        return self.get_slot(var, name)

    def apply_gradients(self, grads_and_vars, name=None, experimental_aggregate_gradients=True):
        for grad, var in grads_and_vars:
            if grad is not None:
                self._resource_apply_dense(grad, var)

        return self._create_updates(grads_and_vars)

    def _create_updates(self, grads_and_vars):
        # Custom logic to generate updates after applying gradients
        updates = []
        for grad, var in grads_and_vars:
            if grad is not None:
                updates.append((var, var - self._learning_rate * grad))
        return updates
