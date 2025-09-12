import tensorflow as tf

# Define a function
def square(x):
    return x**2

# Create a tensor with unstacked elements
elems = tf.constant([3, 7, 4])
unstacked = tf.unstack(elems, axis=0)

# Define `map_fn` equivalent using `tf.vectorized_map` or `tf.map_fn_v2` but those are deprecated. 
# Instead, use `tf.nest.map` in combination with `tf.data.Dataset`, by narrowing down unstacked dataset.
# We need to create a tf.data.Dataset.from_tensor_slices, then use `tf.data.Dataset.map`, the changed Dataset is then converted to `tf.nest.map`.
# In this game, `unstacked` is a list, change the list into Dataset
unstacked_dataset = tf.data.Dataset.from_tensor_slices(tf.data.Dataset.from_tensor_slices(unstacked))
elems_result = tf.nest.map(unstacked_dataset.map(square).get_next)
