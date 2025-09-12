import tensorflow as tf

class SDCAOptimizer(tf.keras.optimizers.Optimizer):
    def __init__(self, learning_rate=0.01, **kwargs):
        super(SDCAOptimizer, self).__init__(name="SDCAOptimizer", **kwargs)
        self.learning_rate = learning_rate

    def _create_slots(self, var_list):
        for var in var_list:
            self.add_slot(var, "dual")

    def _resource_apply_dense(self, grad, var, apply_state=None):
        dual = self.get_slot(var, "dual")
        dual.assign(dual - self.learning_rate * grad)
        var.assign(var - self.learning_rate * dual)

    def _resource_apply_sparse(self, grad, var, indices, apply_state=None):
        dual = self.get_slot(var, "dual")
        dual.assign(dual - self.learning_rate * tf.IndexedSlices(grad, indices))
        var.assign(var - self.learning_rate * dual)

# Usage example
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(None, 5)),
    tf.keras.layers.Dense(1)
])

optimizer = SDCAOptimizer(learning_rate=0.01)
model.compile(optimizer=optimizer, loss='mse')
