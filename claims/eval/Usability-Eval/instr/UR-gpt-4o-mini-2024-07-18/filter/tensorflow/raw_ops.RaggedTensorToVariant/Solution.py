import tensorflow as tf

# Creating a sample RaggedTensor
row_splits = [[0, 2, 5], [0, 3, 5]]
values = [[1, 2], [3, 4, 5], [6, 7], [8, 9, 10]]
ragged_tensor = tf.ragged.RaggedTensor.from_nested_row_splits(values, row_splits)

# Convert RaggedTensor to a Variant Tensor
variant_tensor = tf.convert_to_tensor(ragged_tensor)

# To demonstrate, we can print the variant tensor
print(variant_tensor)
