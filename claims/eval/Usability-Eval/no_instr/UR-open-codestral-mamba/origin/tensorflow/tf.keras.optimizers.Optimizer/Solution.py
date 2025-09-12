import tensorflow as tf

class AbstractOptimizer(tf.keras.optimizers.Optimizer):
    """Abstract base class for optimizers."""

    def __init__(self, name, **kwargs):
        super(AbstractOptimizer, self).__init__(name, **kwargs)

    @classmethod
    def from_config(cls, config):
        return cls(**config)

    def get_config(self):
        return {
            'learning_rate': self._serialize_hyperparameter('learning_rate'),
            'name': self._name,
        }
