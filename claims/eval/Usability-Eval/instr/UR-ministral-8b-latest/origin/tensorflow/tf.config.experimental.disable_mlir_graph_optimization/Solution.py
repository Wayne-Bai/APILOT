import tensorflow as tf

# Disable experimental MLIR-Based TensorFlow Compiler Optimizations
tf.config.optimizer._search_library.set_reduction_threshold(0)

print("Experimental MLIR-Based TensorFlow Compiler Optimizations disabled.")
