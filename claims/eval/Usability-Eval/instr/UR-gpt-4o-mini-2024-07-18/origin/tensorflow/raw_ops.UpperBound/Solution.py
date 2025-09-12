import tensorflow as tf

def upper_bound(sorted_search_values, values):
    # Convert inputs to tensors
    sorted_search_values = tf.convert_to_tensor(sorted_search_values)
    values = tf.convert_to_tensor(values)

    # Find upper bounds using tf.searchsorted
    upper_bounds = tf.searchsorted(sorted_search_values, values, side='right')

    return upper_bounds

# Example usage
sorted_array = [1, 3, 5, 7, 9]
values_array = [0, 2, 5, 6, 10]

upper_bounds_result = upper_bound(sorted_array, values_array)
print(upper_bounds_result.numpy())
