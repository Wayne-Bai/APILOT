
import tensorflow as tf
from tensorflow.python.compiler.mlir import mlir_tensorflow

# Enable experimental MLIR-based TensorFlow compiler optimizations
mlir_tensorflow.enable_experimental_mlir_based_optimizer()
