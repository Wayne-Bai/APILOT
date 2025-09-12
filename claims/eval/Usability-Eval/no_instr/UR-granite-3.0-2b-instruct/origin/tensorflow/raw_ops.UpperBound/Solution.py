import tensorflow as tf

# Assuming sorted_search_values and values are already defined

# Create a sparse tensor from sorted_search_values and values
sparse_tensor = tf.sparse.from_dense(sorted_search_values, values)

# Apply upper_bound along each row
result = tf.raw_ops.UpperBound(sparse_tensor, tf.ones_like(sorted_search_values))

# Convert the result back to a dense tensor if needed
dense_result = result.to_dense()
