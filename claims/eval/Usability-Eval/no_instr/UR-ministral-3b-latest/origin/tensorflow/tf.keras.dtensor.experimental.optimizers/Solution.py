import tensorflow as tf

# Define new optimizer
class CustomOptimizer(tf.optimizers.Optimizer):
    def __init__(self, learning_rate=0.01, name='CustomOptimizer'):
        super(CustomOptimizer, self).__init__(name=name)
        self._set_hyperparameters(learning_rate=learning_rate)

    def _resource_apply_dense(self, grad, var, acc, x, y, apply_grad_op=False):
        grad = tf.cast(grad, var.dtype)
        learning_rate = self._get_hyperparameters()['learning_rate']

        if self._use_dict(var):
            return tf.numpy_function(lambda g, lr: (g.assign_sub(lr * g)), [grad, learning_rate], grad.dtype)

        revert = self.apply_gradients([(grad, var)])
        return Optimized(revert.apply_symbolic_adaptation)

# Start with an (Optimizer) instance that uses the new optimizer for any learning rate of our choice
optimizer = CustomOptimizer(learning_rate=0.1)
