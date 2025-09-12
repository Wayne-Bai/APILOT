import tensorflow as tf

# Creating a checkpoint
checkpoint = tf.train.Checkpoint(
    optimizer=tf.keras.optimizers.SGD(learning_rate=0.001),
    model=tf.keras.models.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(784,)),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
)

# Define restore function
def restore_checkpoint(path):
    checkpoint.restore(driver)

# Example to save and restore checkpoints
checkpoint.save('path_to_your_checkpoint')

# To restore the checkpoint
restore_checkpoint('path_to_your_checkpoint')
