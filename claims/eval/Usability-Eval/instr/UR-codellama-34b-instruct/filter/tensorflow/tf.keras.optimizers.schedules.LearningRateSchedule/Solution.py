
import tensorflow as tf

class LearningRateSchedule(tf.keras.callbacks.Callback):
    def __init__(self, initial_learning_rate, decay_rate, step_size):
        super().__init__()
        self.initial_learning_rate = initial_learning_rate
        self.decay_rate = decay_rate
        self.step_size = step_size

    def on_train_batch_begin(self, batch, logs=None):
        if self.model.optimizer is not None:
            lr = self.model.optimizer.lr.numpy()
            new_lr = max(lr * (1 - decay_rate), 0)
            self.model.optimizer.learning_rate = new_lr

    def on_train_batch_end(self, batch, logs=None):
        if self.model.optimizer is not None:
            lr = self.model.optimizer.lr.numpy()
            new_lr = max(lr * (1 + decay_rate), 0)
            self.model.optimizer.learning_rate = new_lr
