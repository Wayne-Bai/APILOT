import tensorflow as tf

# Assuming you have a tensor 'a'
# Define the shape of the tensor
shape = [2, 3]

# Create a tensor of zeros with the desired shape
a = tf.zeros(shape)

# Transpose the tensor
transposed_a = tf.transpose(a)
