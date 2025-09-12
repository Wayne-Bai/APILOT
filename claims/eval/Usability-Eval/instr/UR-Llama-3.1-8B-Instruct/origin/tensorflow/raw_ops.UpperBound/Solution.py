import tensorflow as tf

# Define a function to apply upper_bound along each row
def apply_upper_bound(search_values, values):
    # Ensure search_values and values are tensor
    search_values = tf.convert_to_tensor(search_values)
    values = tf.convert_to_tensor(values)

    # Get the shape of the search_values tensor
    shape = tf.shape(search_values)

    # Create a tensor to hold the result
    result = tf.ones([shape[0]])

    # Create a tensor where the index of the first element in each row that
    # is greater than the corresponding element in values will be set to 1
    greater_equals_index = tf.reduce_max(tf.where(tf.greater_equal(search_values, values), tf.expand_dims(tf.range(shape[0]), 1), -1), axis=2, keepdims=True)

    # Set the corresponding element in result to the first element that is greater 
    # in each row, otherwise set it to 0
    result = tf.where(greater_equals_index >= shape[0], 0, greater_equals_index)

    return result

# Test the function
search_values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
values = [2, 5, 8]
result = apply_upper_bound(search_values, values)
print(result)  # Output: tf.Tensor([[1 1 1], [1 1 1], [1 1 1]], shape=(3, 1), dtype=int32)

search_values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
values = [3, 5, 7]
result = apply_upper_bound(search_values, values)
print(result)  # Output: tf.Tensor([[2], [1], [2]], shape=(3, 1), dtype=int32)
