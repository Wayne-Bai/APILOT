
import tensorflow as tf

# Set up the TensorBoard visualization
tb = tf.keras.callbacks.TensorBoard(log_dir='./logs', histogram_freq=1, batch_size=32)
