import tensorflow as tf

# Disable the experimental MLIR-based TensorFlow Compiler Optimizations
tf.config.experimental.enable_mlir_graph_optimization(False)
