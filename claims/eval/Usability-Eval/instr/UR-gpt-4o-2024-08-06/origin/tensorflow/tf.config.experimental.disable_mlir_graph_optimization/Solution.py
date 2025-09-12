import tensorflow as tf

# Set the environment variable to disable MLIR-based optimizations
import os
os.environ['TF_DISABLE_MLIR_OPTIMIZATION'] = '1'

# Example to create a session to ensure TensorFlow starts with the environment variable
tf.compat.v1.Session()
