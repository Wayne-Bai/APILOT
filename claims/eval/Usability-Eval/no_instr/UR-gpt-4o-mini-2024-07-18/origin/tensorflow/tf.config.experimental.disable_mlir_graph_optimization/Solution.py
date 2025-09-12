import tensorflow as tf

# Disable experimental MLIR-based TensorFlow compiler optimizations
tf.config.experimental_enable_mlir_graph_optimization(False)

# Your TensorFlow model or operations go here
