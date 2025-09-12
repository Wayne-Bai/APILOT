import tensorflow as tf

class CustomLearningRateSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
    def __init__(self, learning_rate_max, learning_rate_min, decay_steps, alpha=0.5, last_epoch=-1):
        self.learning_rate_max = learning_rate_max
        self.learning_rate_min = learning_rate_min
        self.decay_steps = decay_steps
        self.alpha = alpha
        super(CustomLearningRateSchedule, self).__init__(last_epoch=last_epoch)

    def __call__(self, step):
        # Exponential decay with factor alpha
        decayed_lr = tf.math.exp(-self.alpha * step / self.decay_steps)
        # Linear interpolation between min and max learning rates
        interpolated_lr = self.learning_rate_min + (self.learning_rate_max - self.learning_rate_min) * decayed_lr
        return interpolated_lr
