
import tensorflow as tf

class AbstractOptimizer(object):
    def __init__(self, learning_rate=0.001):
        self._learning_rate = learning_rate

    @property
    def learning_rate(self):
        return self._learning_rate

    @learning_rate.setter
    def learning_rate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Learning rate must be a number.")
        self._learning_rate = value

    def get_config(self):
        return {"learning_rate": self.learning_rate}

    def from_config(cls, config):
        return cls(**config)
