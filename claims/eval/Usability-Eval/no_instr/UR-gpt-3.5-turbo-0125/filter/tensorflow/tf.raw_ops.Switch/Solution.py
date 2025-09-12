
import tensorflow as tf

@tf.function
def forward_data(pred, data):
    return tf.raw_ops.Method(pred=pred, data=data)

# Example usage
pred = tf.constant(True)
data = tf.constant([1, 2, 3])
output = forward_data(pred, data)
print(output)
