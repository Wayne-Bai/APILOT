import tensorflow as tf

# Disable experimental MLIR-Based TensorFlow Compiler Optimizations
tf.config.experimental.enable_mlir_graph_optimization(False)
