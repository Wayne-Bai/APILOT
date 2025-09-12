
import tensorflow as tf

class AbstractOptimizer(tf.keras.optimizers.Optimizer):
    def __init__(self, learning_rate=0.1, **kwargs):
        super().__init__(name="Abstract Optimizer", **kwargs)
        self.learning_rate = tf.cast(learning_rate, dtype=tf.float32)

    @abstractmethod
    def get_updates(self, params, model):
        """
        Returns a list of update operations required for the optimizer.
        :param params: A list of parameters to be optimized.
        :param model: The model object that contains information about the weights and biases.
        :return: A list of update operations.
        """
