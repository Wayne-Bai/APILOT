import tensorflow as tf

class LearningRateSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
    def __init__(self, initial_learning_rate, decay_steps, decay_rate):
        super(LearningRateSchedule, self).__init__()
        self.initial_learning_rate = initial_learning_rate
        self.decay_steps = decay_steps
        self.decay_rate = decay_rate

    def __call__(self, step):
        # Calculate the learning rate based on exponential decay
        return self.initial_learning_rate * (self.decay_rate ** (step / self.decay_steps))

    def get_config(self):
        return {
            'initial_learning_rate': self.initial_learning_rate,
            'decay_steps': self.decay_steps,
            'decay_rate': self.decay_rate
        }
