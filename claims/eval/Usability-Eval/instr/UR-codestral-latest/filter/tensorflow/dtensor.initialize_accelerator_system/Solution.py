import tensorflow as tf

# Disable all GPUs
tf.config.set_visible_devices([], 'GPU')

# Initialize DTensor
# This will ensure all CPU cores are used for computations
dtensor = tf.experimental.dtensor.create_dtensor([1])
sharding = tf.experimental.dtensor. distribute(dtensor, tf.experimental.dtensor.unstack(tf.range(8)))

# Validate the initial setup
with tf.device(sharding.device):
  print(tf.range(8))
