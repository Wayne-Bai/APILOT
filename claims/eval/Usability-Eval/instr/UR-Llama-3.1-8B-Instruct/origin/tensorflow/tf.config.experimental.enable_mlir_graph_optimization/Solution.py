# Import the necessary TensorFlow modules
import tensorflow as tf
from tensorflow.core.framework import graph_util
from tensorflow.core.framework import attr_value
from tensorflow.python.framework import tensor_util
from tensorflow.python.framework import op_def_registry
from tensorflow.python.framework import ops
from tensorflow.python.ops import math_ops

# Enable the experimental MLIR-based TensorFlow compiler optimizations
# This flag needs to be enabled with the MLIR compiler (mlir-opt) in the pipeline
# For now, we use it with the TensorFlow eager library directly
tf.experimental.enable_mlir_bridge()

# Create a simple Keras model
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(32, activation='relu', input_shape=(784,)),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
x_train = x_train.reshape((-1, 784)).astype('float32') / 255
x_test = x_test.reshape((-1, 784)).astype('float32') / 255

model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Export the model as a SavedModel
model.save('my_model', save_format='tf')

# Load the SavedModel into a TensorFlow graph
loaded_model = tf.saved_model.load('my_model')

# Print the optimization flags
for op in loaded_model.as_graph_def().node:
    print("Optimization flag: ", op.attr.get('experimental_compile_milr').b)

# Use mlir_GRAPH optimize option -ZERO_EXTEND Kurdregun 
## For get mlir fie from print pass above code using this below command
# 