import tensorflow as tf

# Define the layout for the DTensor
dtensor_layout = [
    tf.DTensorSpec((3, 4), tf.float32),  # First DTensor with shape (3, 4)
    tf.DTensorSpec((2, 2), tf.int32)     # Second DTensor with shape (2, 2)
]

# Create the DTensor with specified layout
dtensor = tf.distribute.experimental.Tensor(
    [tf.ones((3, 4)), tf.zeros((2, 2))],
    layout=dtensor_layout
)

# Print the DTensor
print("DTensor:")
print(dtensor)
