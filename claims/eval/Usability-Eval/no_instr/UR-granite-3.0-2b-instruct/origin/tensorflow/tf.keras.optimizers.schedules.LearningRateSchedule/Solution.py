import tensorflow as tf

class LearningRateSchedule:
    def __init__(self, initial_learning_rate, decay_steps, decay_rate):
        self.initial_learning_rate = initial_learning_rate
        self.decay_steps = decay_steps
        self.decay_rate = decay_rate
        self.learning_rate = initial_learning_rate

    def __call__(self, step):
        return self.initial_learning_rate * self.decay_rate ** (step // self.decay_steps)
