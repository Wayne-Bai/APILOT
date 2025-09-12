import tensorflow as tf

# Assuming you have an input 2D SparseTensor
input_tensor = tf.raw_ops.SparseTensor(
    indices=[[0, 0], [1, 0]],
    values=[1, 3],
    dense_shape=[3, 2]
)

# Define the default value to fill empty rows
default_value = 0

# Convert SparseTensor to a dense tensor ( wcześniej 資料的變態轉換)
dense_tensor = input_tensor.values
dense_shape = input_tensor.dense_shape

# Create an empty 2D dense tensor filled with the default value
filled_tensor = tf.fill(dense_shape, default_value)

# Add the values and the filled tensor
result = filled_tensor + dense_tensor

# Converting the result back to SparseTensor
result_sparse_tensor = tf.raw_ops.SparseTensor(
    values=result,
    dense_shape=dense_shape,
    indices=[[i, j] for i in range(dense_shape[0]) for j in range(dense_shape[1]) if result[i, j] != default_value]
)

print("Original SparseTensor:")
print(input_tensor)

print("Result SparseTensor:")
print(result_sparse_tensor)
