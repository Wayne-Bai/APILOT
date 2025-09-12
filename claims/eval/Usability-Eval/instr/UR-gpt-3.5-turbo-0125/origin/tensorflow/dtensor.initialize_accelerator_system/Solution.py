
import tensorflow as tf

# Initialize accelerators and communication fabrics for DTensor
tf.config.experimental_connect_to_cluster()
tf.tpu.experimental.initialize_tpu_system()
