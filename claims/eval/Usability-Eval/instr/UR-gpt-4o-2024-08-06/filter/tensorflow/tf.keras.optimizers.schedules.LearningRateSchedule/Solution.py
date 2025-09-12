import tensorflow as tf

class CustomLearningRateSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
    def __init__(self, initial_learning_rate, decay_steps, decay_rate, staircase=False):
        super(CustomLearningRateSchedule, self).__init__()
        self.initial_learning_rate = initial_learning_rate
        self.decay_steps = decay_steps
        self.decay_rate = decay_rate
        self.staircase = staircase

    def __call__(self, step):
        if self.staircase:
            exponent = tf.math.floor(step / self.decay_steps)
        else:
            exponent = step / self.decay_steps
        return self.initial_learning_rate * tf.math.pow(self.decay_rate, exponent)

# Example usage.
initial_learning_rate = 0.1
decay_steps = 1000
decay_rate = 0.96

lr_schedule = CustomLearningRateSchedule(initial_learning_rate, decay_steps, decay_rate)

# Apply this custom learning rate schedule to an optimizer
optimizer = tf.keras.optimizers.Adam(learning_rate=lr_schedule)

# You can also see how the learning rate changes with steps.
for step in range(0, 5000, 1000):
    lr = lr_schedule(step)
    print(f"Step {step}: learning rate = {lr.numpy()}")
