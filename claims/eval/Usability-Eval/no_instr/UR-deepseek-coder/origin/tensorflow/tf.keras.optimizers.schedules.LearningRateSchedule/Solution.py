import tensorflow as tf

class LearningRateSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
    def __init__(self, initial_learning_rate):
        super(LearningRateSchedule, self).__init__()
        self.initial_learning_rate = initial_learning_rate

    def __call__(self, step):
        # Example: A simple linear decay schedule
        decay_rate = 0.1
        return self.initial_learning_rate * (1 / (1 + decay_rate * step))

    def get_config(self):
        return {"initial_learning_rate": self.initial_learning_rate}

# Example usage:
# lr_schedule = LearningRateSchedule(initial_learning_rate=0.1)
# optimizer = tf.keras.optimizers.Adam(learning_rate=lr_schedule)
