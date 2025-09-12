import tensorflow as tf
from tensorflow.python.ops import resource_variable

class AbstractOptimizer(tf.keras.optimizers.Optimizer):
    """Abstract optimizer base class."""

    def __init__(self, name='abstract_optimizer', **kwargs):
        """
        Constructs a new Optimizer instance.

        Args:
          name: A name for the optimization algorithm.
          **kwargs: Additional keyword arguments.
        """
        super(AbstractOptimizer, self).__init__(name, **kwargs)
        self.iterator = tf.keras.backend.get_variable(
            name='iterator',
            shape=[],
            dtype=tf.int32,
            trainable=False,
            initializer=resource_variable.initializer(0))
        self.learning_rate = kwargs.get('learning_rate', 0.01)

    def _resource_optimizer(self):
        """
        This method should be overridden by subclasses to create their own
        resource variable list.
        """
        raise NotImplementedError

    def _resource_runs(self):
        """
        This method should be overridden by subclasses to create the runs.
        """
        raise NotImplementedError

    def apply_gradients(self, grads_and_vars, name=None, experimental_aggregate_gradients=None, experimental_batching=None):
        grads, vars = zip(*grads_and_vars)
        if self.experimental_aggregate_gradients:
            batched_grads = tf.stack(grads, axis=-1)
        else:
            batched_grads = grads

        increment = tf.cast(tf.convert_to_tensor(self._resource_runs(iterator=self.iterator)), tf.float32)
        new_iterator = tf.slice(self.iterator, [0], [tf.shape(self.iterator)[0] + 1])
        self.iterator.assign(new_iterator)

        resource_optimizer = self._resource_optimizer()
        return resource_optimizer.apply(batched_grads, experimental_batching=experimental_batching)
