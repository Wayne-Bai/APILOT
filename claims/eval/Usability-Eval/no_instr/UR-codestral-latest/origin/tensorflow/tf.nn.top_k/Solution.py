import tensorflow as tf

def find_k_largest(tensor, k):
    # Get the values using tf.nn.top_k() function and transpose the results
    values, indices = tf.nn.top_k(tensor, k=k, sorted=False)

    # Return the values and indices
    return values, indices

# Testing the function
tensor = tf.constant([[1, 5, 3], [6, 2, 7]])
k = 2
result_values, result_indices = find_k_largest(tensor, k)

with tf.Session() as sess:
    values, indices = sess.run([result_values, result_indices])
    print("Values: ", values)
    print("Indices: ", indices)
