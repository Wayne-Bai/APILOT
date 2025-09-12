import tensorflow as tf

# Assuming pred is a tensor that decides which output port to use
pred = tf.constant([True, False])

# Assuming data1 and data2 are tensors to be switched based on pred
data1 = tf.constant([1, 2, 3])
data2 = tf.constant([4, 5, 6])

# Use tf.where to switch the data based on the pred tensor
output = tf.where(pred, data1, data2)

# Print output
print(output)
