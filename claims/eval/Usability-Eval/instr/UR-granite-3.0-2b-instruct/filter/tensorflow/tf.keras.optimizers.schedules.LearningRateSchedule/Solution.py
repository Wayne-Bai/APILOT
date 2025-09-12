import tensorflow as tf

class LearningRateSchedule:
    def __init__(self, initial_learning_rate, decay_steps, decay_rate):
        self.initial_learning_rate = initial_learning_rate
        self.decay_steps = decay_steps
        self.decay_rate = decay_rate
        self.learning_rate = initial_learning_rate

    def __call__(self, step):
        learning_rate = self.initial_learning_rate * self.decay_rate ** (step // self.decay_steps)
        return learning_rate

# Example usage:
initial_learning_rate = 0.01
decay_steps = 10000
decay_rate = 0.9

lr_schedule = LearningRateSchedule(initial_learning_rate, decay_steps, decay_rate)

# Assuming you have a optimizer and a global step variable
optimizer = tf.keras.optimizers.Adam()
global_step = tf.Variable(0, trainable=False)

# Update the learning rate at each step
with tf.control_dependencies([global_step.assign_add(1)]):
    updated_lr = lr_schedule(global_step)
    optimizer.apply_gradients(zip(model.trainable_variables, [updated_lr]))
