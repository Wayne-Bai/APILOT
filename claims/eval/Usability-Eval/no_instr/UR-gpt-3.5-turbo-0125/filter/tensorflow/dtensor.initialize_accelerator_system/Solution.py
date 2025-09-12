
import tensorflow as tf

# Initializes accelerators and communication fabrics for DTensor
tf.config.experimental.set_visible_devices([], 'GPU')
