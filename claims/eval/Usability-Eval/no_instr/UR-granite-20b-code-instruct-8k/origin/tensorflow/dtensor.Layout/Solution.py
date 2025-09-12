import tensorflow as tf

# Define the layout information
layout = tf.experimental.dtensor.Layout.replicated(2)

# Print the layout information
print(layout)
