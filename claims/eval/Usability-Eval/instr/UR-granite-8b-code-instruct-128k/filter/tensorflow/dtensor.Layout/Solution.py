import tensorflow as tf

# Create a DTensor
dtensor = tf.ragged.constant([[1, 2], [3, 4], [5, 6]])

# Print the layout information
print("DTensor layout information:")
print("Rank:", dtensor.ragged_rank)
print("Shape:", dtensor.shape)
print("Row splits:", dtensor.row_splits)
print("Value row ids:", dtensor.value_rowids())
