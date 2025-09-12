import tensorflow as tf

class AbstractOptimizer(object):
  """Abstract optimizer base class."""

  def __init__(self, name, learning_rate):
    """Initialize an `AbstractOptimizer` object.

    Args:
      name: A string. The name to use for the optimizer.
      learning_rate: A `Tensor` or a floating point value.  The learning rate.
    """
    self._name = name
    self._learning_rate = learning_rate

  @property
  def name(self):
    return self._name

  @property
  def learning_rate(self):
    return self._learning_rate

  def apply_gradients(self, grads_and_vars, global_step=None, name=None):
    """Apply gradients to variables.

    This method simply computes the gradients and calls `apply_gradients`.
    Therefore, `apply_gradients` can not be implemented in terms of this method.
    However, the implementation can be written in terms of this method if
    the algorithm can be applied to the entire gradient tensor (e.g., normal
    SGD). Otherwise, `apply_gradients` should be implemented directly,
    using `compute_gradients`.

    Args:
      grads_and_vars: List of (gradient, variable) pairs as returned by
        `compute_gradients`.
      global_step: Optional `Variable` to increment by one after the
        variables have been updated.
      name: Optional name for the returned operation.  Default to the
        name passed to the `Optimizer` constructor.

    Returns:
      An `Operation` that applies the specified gradients. If `global_step`
      is not `None`, that operation also increments `global_step`.

    Raises:
      TypeError: If `grads_and_vars` is not a list or tuple.
      ValueError: If `global_step` is not `None` and is not a `Variable`.
    """

