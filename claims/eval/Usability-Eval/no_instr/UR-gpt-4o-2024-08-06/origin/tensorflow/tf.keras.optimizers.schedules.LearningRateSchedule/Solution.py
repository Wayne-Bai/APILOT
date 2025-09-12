import tensorflow as tf

class MyLearningRateSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
    def __init__(self, initial_learning_rate, decay_steps, decay_rate, staircase=False):
        super(MyLearningRateSchedule, self).__init__()
        self.initial_learning_rate = initial_learning_rate
        self.decay_steps = decay_steps
        self.decay_rate = decay_rate
        self.staircase = staircase

    def __call__(self, step):
        if self.staircase:
            # Apply staircase decay
            decay_step = step // self.decay_steps
        else:
            # Continuous decay
            decay_step = step / self.decay_steps
        
        return self.initial_learning_rate * tf.math.pow(self.decay_rate, decay_step)

# Example usage
initial_learning_rate = 0.1
decay_steps = 100
decay_rate = 0.96
learning_rate_schedule = MyLearningRateSchedule(initial_learning_rate, decay_steps, decay_rate, staircase=True)

# You would use the learning rate schedule in your optimizer like this:
optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate_schedule)
