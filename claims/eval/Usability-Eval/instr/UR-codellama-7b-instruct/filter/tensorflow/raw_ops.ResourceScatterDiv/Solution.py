
import tensorflow as tf

# Create a constant tensor for the variable reference
variable = tf.constant(0)

# Define the sparse updates
updates = tf.SparseTensor(indices=[[1, 2], [3, 4]], values=[5, 6], dense_shape=[5, 5])

# Divide the sparse updates into the variable reference
divisor = tf.raw_ops.Div(a=variable, b=updates)

print(divisor)
