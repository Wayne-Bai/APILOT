import tensorflow as tf

# Creating a tensor with shape (3, 3)
values = tf.random.uniform([3, 3], minval=0, maxval=100)

# Creating a tensor with sorted values
sorted_search_values = tf.sort(tf.matmul(values, tf.ones((3, 3))))

# Using tf.searchsorted to find the index of upper bound along each row
upper_bounds = tf.raw_ops.SearchSorted(
    sorted=sorted_search_values,
    values=values,
    compression=None,
   sorted_right=False)

# print the values to understand
print("values", values)
print("sorted_search_values", sorted_search_values)
print("upper_bounds", upper_bounds)

# Converting the result to integers because searchsorted returns index and maximum index is always one less than the size of the array
result = tf.cast(tf.math.minimum(upper_bounds, shape=values.shape), tf.int32)

print("Result", result)
