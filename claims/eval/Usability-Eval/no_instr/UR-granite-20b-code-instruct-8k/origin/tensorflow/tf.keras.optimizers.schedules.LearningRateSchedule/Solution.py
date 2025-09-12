import tensorflow as tf

class LearningRateSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
  """Abstract base class for learning rate schedules."""

  def __call__(self, step):
    """Applies the learning rate schedule.

    Args:
      step: `int`, the current training step.

    Returns:
      a `Tensor` representing the learning rate value.
    """
    return self.get_config()

  def get_config(self):
    """Returns the configuration of the learning rate schedule."""
    return {}
