
import tensorflow as tf

class LearningRateSchedule(tf.keras.callbacks.Callback):
    def __init__(self, lr_schedule: dict = None):
        self.lr_schedule = lr_schedule or {}

    def on_train_begin(self, logs=None):
        super().on_train_begin(logs)
        self.reset()

    def reset(self):
        self.current_epoch = 0
        self.lr = self.init_lr

    def schedule(self, epoch: int, logs=None):
        pass

    def on_epoch_end(self, epoch, logs=None):
        self.current_epoch += 1
        self.lr = self.schedule(self.current_epoch, logs)
