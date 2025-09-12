import tensorflow as tf

class LearningRateSchedule:
    def __init__(self, initial_learning_rate, decay_steps, decay_rate):
        self.initial_learning_rate = initial_learning_rate
        self.decay_steps = decay_steps
        self.decay_rate = decay_rate
        self.learning_rate = tf.Variable(initial_learning_rate, trainable=False)
        self.global_step = tf.Variable(0, trainable=False)

    def update_learning_rate(self, global_step):
        self.global_step.assign(global_step)
        self.learning_rate.assign(self.initial_learning_rate * self.decay_rate ** tf.math.floor(self.global_step / self.decay_steps))

    def get_learning_rate(self):
        return self.learning_rate
