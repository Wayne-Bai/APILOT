import tensorflow as tf

# Disable MLIR-Based TensorFlow Compiler Optimizations
tf.compat.v1.disable_eager_execution()
tf.compat.v1.disable_mlir_graph_optimization()
