import tensorflow as tf
from tensorflow.keras.optimizers import Optimizer

class CustomOptimizer(Optimizer):
    def __init__(self, learning_rate=0.001, name='CustomOptimizer', **kwargs):
        super(CustomOptimizer, self).__init__(name, **kwargs)
        self._set_hyper('learning_rate', kwargs.get('lr', learning_rate))

    def apply_gradients(self, grads_and_vars, name=None, **kwargs):
        # Implement the logic to update the weights using the gradients
        # For example:
        for grad, var in grads_and_vars:
            if grad is None or var is None:
                continue

            var_update = var - self.learning_rate * grad
            var.assign(var_update)

    def get_config(self):
        base_config = super(CustomOptimizer, self).get_config()
        return {**base_config, 'learning_rate': self._serialize_hyperparameter('learning_rate')}

# Example usage
optimizer = CustomOptimizer(learning_rate=0.01)
