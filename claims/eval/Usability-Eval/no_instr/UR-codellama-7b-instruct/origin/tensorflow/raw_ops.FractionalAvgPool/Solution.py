import tensorflow as tf

# Create a placeholder tensor for the input data
input_data = tf.placeholder(dtype=tf.float32, shape=(None, 10))

# Create a constant tensor for the pool size and stride
pool_size = 4
stride = 2

# Use the raw_ops module to perform fractional average pooling on the input data
output = tf.raw_ops.Pool(input=input_data, pool_size=pool_size, stride=stride, padding="SAME")

print(output)
