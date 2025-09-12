import tensorflow as tf

# Enabling TensorFlow 2.x behavior. (Optional, mandatory for TF 2.x)
tf.compat.v1.disable_eager_execution()

# Enabling the experimental MLIR-based compiler optimizations
tf.config.experimental.enable_mlir_graph_optimization()
