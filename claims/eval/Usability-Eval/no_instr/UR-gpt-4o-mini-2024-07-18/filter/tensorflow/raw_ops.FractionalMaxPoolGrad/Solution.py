import tensorflow as tf

# Assuming the necessary inputs are defined
input_tensor = tf.random.uniform(shape=[1, 4, 4, 1])  # Example input
pool_size = [2, 2]
output_size = [2, 2]

# Perform Fractional Max Pooling
pooled_output, row_indices, col_indices = tf.nn.fractional_max_pool(
    input_tensor, 
    pool_shape=pool_size, 
    fractional_pooling=True, 
    output_shape=output_size
)

# For gradient computation, you would typically perform it in a GradientTape context
with tf.GradientTape() as tape:
    tape.watch(input_tensor)
    pooled_output, row_indices, col_indices = tf.nn.fractional_max_pool(
        input_tensor, 
        pool_shape=pool_size, 
        fractional_pooling=True, 
        output_shape=output_size
    )

# Compute gradients
gradients = tape.gradient(pooled_output, input_tensor)

print("Pooled Output:", pooled_output)
print("Row Indices:", row_indices)
print("Col Indices:", col_indices)
print("Gradients:", gradients)
