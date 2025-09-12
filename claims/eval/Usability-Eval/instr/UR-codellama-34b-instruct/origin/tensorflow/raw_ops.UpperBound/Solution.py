import tensorflow as tf

# Example inputs
sorted_search_values = [[1, 3, 5], [2, 4, 6]]
values = [[0, 7, 8], [1, 4, 9]]

# Define a function to apply upper bound along each row
def apply_upper_bound(sorted_search_values, values):
    # Create a lambda function to apply the upper bound operation
    upper_bound = lambda x: tf.maximum(x[0], x[1])
    
    # Apply the lambda function to each element in the input tensors
    result = tf.map_fn(upper_bound, (sorted_search_values, values), dtype=tf.int32)
    
    return result

# Call the function with the example inputs
output = apply_upper_bound(sorted_search_values, values)

print(output) # [2 4 6]
