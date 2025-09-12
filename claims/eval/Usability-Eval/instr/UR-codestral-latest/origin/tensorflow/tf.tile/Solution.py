import tensorflow as tf

# Let's assume 'x' is the given tensor
x = tf.constant([1, 2, 3])

# 'multiples' is the number of times we want to tile 'x'
multiples = [2, 1]  # It means tile 'x' twice along the first dimension and once along the second dimension

output_tensor = tf.tile(x, multiples)

print(output_tensor)
