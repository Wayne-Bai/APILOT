import tensorflow as tf
from tensorflow.keras.optimizers.schedules import LearningRateSchedule

# Define a custom learning rate schedule class
class CustomLearningRateSchedule(LearningRateSchedule):
    def __init__(self, initial_learning_rate, decay_steps, decay_rate):
        super(CustomLearningRateSchedule, self).__init__()
        self.initial_learning_rate = initial_learning_rate
        self.decay_steps = decay_steps
        self.decay_rate = decay_rate

    @tf.function
    def __call__(self, step):
        return tf.train.exponential_decay(
            self.initial_learning_rate,
            step,
            self.decay_steps,
            self.decay_rate,
            staircase=True
        )

# Instantiate the custom learning rate schedule class
lr_schedule = CustomLearningRateSchedule(initial_learning_rate=0.1, decay_steps=1000, decay_rate=0.96)

# Test the learning rate schedule
step = tf.Variable(0, dtype=tf.int64)
lr = lr_schedule(step)
print(f"Initial learning rate: {lr.numpy()}")
