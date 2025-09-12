import tensorflow as tf
from tensorflow.keras.optimizers import schedules

class LearningRateSchedule(schedules.LearningRateSchedule):

    def __init__(self, initial_learning_rate, decay_steps, decay_rate):

        super(LearningRateSchedule, self).__init__()
        self.initial_learning_rate = initial_learning_rate
        self.decay_steps = decay_steps
        self.decay_rate = decay_rate

    def __call__(self, step):

        return self.initial_learning_rate * self.decay_rate ** (step // self.decay_steps)

# Example of using our LearningRateSchedule
initial_learning_rate = 0.1
decay_steps = 10000
decay_rate = 0.96

lr_schedule = LearningRateSchedule(initial_learning_rate, decay_steps, decay_rate)

# Use the learning rate schedule in an optimizer
opt = tf.keras.optimizers.Adam(learning_rate=lr_schedule)
