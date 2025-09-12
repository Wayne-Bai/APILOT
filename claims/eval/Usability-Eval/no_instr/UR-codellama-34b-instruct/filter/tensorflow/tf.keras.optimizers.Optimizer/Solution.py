import tensorflow as tf

class Optimizer(object):
    """Abstract optimizer base class."""

    def __init__(self, learning_rate=0.01, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self._learning_rate = tf.Variable(learning_rate, name="learning_rate")
        self._beta1 = tf.Variable(beta1, name="beta1")
        self._beta2 = tf.Variable(beta2, name="beta2")
        self._epsilon = tf.Variable(epsilon, name="epsilon")

    def _minimize_loss(self, loss):
        raise NotImplementedError("Subclasses must implement _minimize_loss()")

    def minimize_loss(self, loss, var_list=None):
        """Minimize the given loss function using this optimizer.

        Args:
            loss: The loss function to minimize.
            var_list: List of variables to optimize. Defaults to all trainable variables.

        Returns:
            A tuple `(gradients, variables)` containing gradients and variables.
        """
        gradients = self._minimize_loss(loss)
        return gradients, var_list or tf.trainable_variables()
