import tensorflow as tf

class CustomLearningRateSchedule(tf.keras.optimizers.schedules.LearningRateSchedule):
    def __init__(self, initial_learning_rate):
        self.initial_learning_rate = initial_learning_rate

    def __call__(self, step):
        # Define your custom learning rate schedule logic here
        # Example: decrement learning rate linearly
        return self.initial_learning_rate / (1 + 0.1 * step)
