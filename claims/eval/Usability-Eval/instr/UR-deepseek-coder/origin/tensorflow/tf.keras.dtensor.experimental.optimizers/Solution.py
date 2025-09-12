import tensorflow as tf

class CustomOptimizer(tf.keras.optimizers.Optimizer):
    def __init__(self, learning_rate=0.01, name="CustomOptimizer", **kwargs):
        super(CustomOptimizer, self).__init__(name, **kwargs)
        self._learning_rate = learning_rate

    def _resource_apply_dense(self, grad, var, apply_state=None):
        var_device, var_dtype = var.device, var.dtype.base_dtype
        coefficients = ((apply_state or {}).get((var_device, var_dtype))
                        or self._fallback_apply_state(var_device, var_dtype))

        lr_t = coefficients['lr_t']
        var.assign_sub(lr_t * grad)

    def _resource_apply_sparse(self, grad, var, indices, apply_state=None):
        raise NotImplementedError("Sparse gradient updates are not supported.")

    def get_config(self):
        base_config = super(CustomOptimizer, self).get_config()
        return {**base_config, "learning_rate": self._serialize_hyperparameter("learning_rate")}

# Example usage
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(20,)),
    tf.keras.layers.Dense(1)
])

optimizer = CustomOptimizer(learning_rate=0.01)
model.compile(optimizer=optimizer, loss='mean_squared_error')

# Training data
import numpy as np
x_train = np.random.random((100, 20))
y_train = np.random.random((100, 1))

model.fit(x_train, y_train, epochs=5)
