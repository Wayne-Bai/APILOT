
import tensorflow as tf

# Your code for building and training the model

# Define a TensorBoard callback
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

# Start TensorBoard by running the following command in the terminal or command prompt
# tensorboard --logdir=logs
