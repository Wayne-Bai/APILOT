import tensorflow as tf

# Import the dtensor module
from tensorflow.dtensor import dtensor_module

# Create a new session
session = dtensor_module.create_session()

# Define a computation graph
x = tf.constant(1.0)
y = x * 2.0

# Run the computation graph in the session
result = session.run(y, {})

print("Result:", result)
