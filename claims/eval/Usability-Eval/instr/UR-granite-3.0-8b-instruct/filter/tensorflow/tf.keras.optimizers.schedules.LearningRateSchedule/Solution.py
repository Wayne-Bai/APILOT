import tensorflow as tf

class CustomLearningRateSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
    def __init__(self, initial_learning_rate, decay_steps, decay_rate):
        self.initial_learning_rate = initial_learning_rate
        self.decay_steps = decay_steps
        self.decay_rate = decay_rate

    def __call__(self, step):
        return self.initial_learning_rate * tf.math.exp(-self.decay_rate * step / self.decay_steps)

# Usage
initial_learning_rate = 0.1
decay_steps = 1000
decay_rate = 0.9
learning_rate_schedule = CustomLearningRateSchedule(initial_learning_rate, decay_steps, decay_rate)

# Assuming you have a model and a optimizer
model = ...
optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate_schedule)
