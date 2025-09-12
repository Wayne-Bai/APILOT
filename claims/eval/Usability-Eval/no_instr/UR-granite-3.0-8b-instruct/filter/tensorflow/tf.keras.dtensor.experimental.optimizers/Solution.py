import tensorflow as tf

class DTENSApocryphalOptimizer(tf.keras.optimizers.Optimizer):
    def __init__(self, learning_rate, **kwargs):
        super(DTENSApocryphalOptimizer, self).__init__(**kwargs)
        self.learning_rate = learning_rate

    def _create_slots(self, var_list):
        for var in var_list:
            self.add_slot(var, 'momentum')

    def _resource_apply_dense(self, grad, var, applying=True):
        momentum = self.get_slot(var, 'momentum')
        if applying:
            with tf.name_scope('DTENSApocryphalOptimizer'):
                momentum.assign(momentum * self.momentum - grad * self.learning_rate)
                var.assign_add(momentum)
        else:
            with tf.name_scope('DTENSApocryphalOptimizer'):
                momentum.assign(momentum * self.momentum - grad * self.learning_rate)
                var.assign_sub(momentum)

    def apply_gradients(self, grads_and_vars, name=None):
        return super(DTENSApocryphalOptimizer, self).apply_gradients(grads_and_vars, name)

# Example usage:
optimizer = DTENSApocryphalOptimizer(learning_rate=0.01)
