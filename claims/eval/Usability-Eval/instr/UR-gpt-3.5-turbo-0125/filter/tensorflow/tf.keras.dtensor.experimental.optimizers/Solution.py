
import tensorflow as tf

# Create custom optimizer using tf.keras.optimizers.OptimizerV2 as a base class
class CustomOptimizer(tf.keras.optimizers.OptimizerV2):
    
    def __init__(self, learning_rate=0.001):
        super(CustomOptimizer, self).__init__('CustomOptimizer')
        self.learning_rate = learning_rate

    def get_config(self):
        config = super(CustomOptimizer, self).get_config()
        config.update({
            'learning_rate': self.learning_rate
        })
        return config

    def _resource_apply_dense(self, grad, var):
        var_dtype = var.dtype.base_dtype
        lr = tf.convert_to_tensor(self.learning_rate, var_dtype)
        new_var = var - lr * grad
        return var.assign(new_var)

# Example usage of the custom optimizer
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(10, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

optimizer = CustomOptimizer(learning_rate=0.01)
model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
