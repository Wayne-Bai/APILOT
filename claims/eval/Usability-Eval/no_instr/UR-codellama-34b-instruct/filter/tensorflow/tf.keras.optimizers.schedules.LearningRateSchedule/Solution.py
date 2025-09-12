
import tensorflow as tf

class LearningRateSchedule(tf.keras.callbacks.Callback):
    def __init__(self, initial_learning_rate, learning_rate_decay, decay_steps):
        super(LearningRateSchedule, self).__init__()
        self.initial_learning_rate = initial_learning_rate
        self.learning_rate_decay = learning_rate_decay
        self.decay_steps = decay_steps

    def on_epoch_begin(self, epoch, logs=None):
        if epoch % self.decay_steps == 0:
            new_learning_rate = self.initial_learning_rate * (1 / (1 + self.learning_rate_decay)) ** (epoch // self.decay_steps)
            tf.keras.backend.set_value(self.model.optimizer.lr, new_learning_rate)
