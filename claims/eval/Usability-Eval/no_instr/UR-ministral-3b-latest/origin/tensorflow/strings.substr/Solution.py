import tensorflow as tf

# Create a tensor of strings.
str_tensor = tf.constant(['abc', 'def', 'ghi', 'jkl'])

# Create a length tensor for each string in the input tensor.
lengths = tf.reduce_sum(
    tf.strings.split(str_tensor, "\n"),
    axis=-1
)

# Get the start index.
start_indices = tf.strings.to_hash_bucket(nums=9, slots_per_group=1024, limit=0)

# Create a mask for strings longer than the desired length.
mask = tf.strings.length(str_tensor) > 1

# Split the tensor of strings using the start index and mask.
split_tensor = tf.strings.split(str_tensor, delimiter="")

# Combine the results into a single string tensor.
output_tensor = tf.strings.join(joiner="", values=split_tensor)
