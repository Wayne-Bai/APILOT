
import tensorflow as tf

class LearningRateSchedule(tf.keras.callbacks.Callback):
    """The learning rate schedule base class.

    This callback adjusts the learning rate of the model during training.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.learning_rate = 0.01

    def on_train_begin(self, logs=None):
        self.learning_rate = tf.keras.optimizers.schedules.ExponentialDecay(
            initial_learning_rate=0.01,
            decay_steps=100,
            decay_rate=0.9,
            staircase=True)

    def on_epoch_begin(self, epoch, logs=None):
        if epoch > 5:
            self.learning_rate = tf.keras.optimizers.schedules.InverseTimeDecay(
                initial_learning_rate=0.01,
                decay_steps=100,
                decay_rate=0.9,
                staircase=True)
        else:
            self.learning_rate = tf.keras.optimizers.schedules.CosineDecay(
                initial_learning_rate=0.01,
                decay_steps=100,
                alpha=0.9)
