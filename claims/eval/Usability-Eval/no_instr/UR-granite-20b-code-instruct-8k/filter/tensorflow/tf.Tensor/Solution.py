import tensorflow as tf

# Define a 3-dimensional tensor (matrix) with 5 rows, 4 columns and 3 channels
tensor = tf.constant([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                      [[13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]],
                      [[25, 26, 27], [28, 29, 30], [31, 32, 33], [34, 35, 36]],
                      [[37, 38, 39], [40, 41, 42], [43, 44, 45], [46, 47, 48]],
                      [[49, 50, 51], [52, 53, 54], [55, 56, 57], [58, 59, 60]]], tf.int32)

# Print the shape of the tensor
print(tensor.shape)

# Output:
# (5, 4, 3)
