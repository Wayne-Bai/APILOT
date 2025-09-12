import tensorflow as tf

class DTensorOptimizer(tf.keras.optimizers.Optimizer):
    def __init__(self, optimizer, mesh, **kwargs):
        super(DTensorOptimizer, self).__init__(**kwargs)
        self.optimizer = optimizer
        self.mesh = mesh

    def apply_gradients(self, grads_and_vars, name=None):
        # Apply gradients using the underlying optimizer
        return self.optimizer.apply_gradients(grads_and_vars, name=name)

    def get_config(self):
        config = super(DTensorOptimizer, self).get_config()
        config.update({
            'optimizer': tf.keras.optimizers.serialize(self.optimizer),
            'mesh': self.mesh
        })
        return config

    @classmethod
    def from_config(cls, config):
        optimizer = tf.keras.optimizers.deserialize(config.pop('optimizer'))
        mesh = config.pop('mesh')
        return cls(optimizer, mesh, **config)

# Example usage:
# mesh = ...  # Define your DTensor mesh
# optimizer = DTensorOptimizer(tf.keras.optimizers.Adam(), mesh)
# model.compile(optimizer=optimizer, loss='mse')
