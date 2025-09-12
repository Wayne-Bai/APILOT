import tensorflow as tf

# Define the input logits
logits = tf.constant([[0.25, 0.5, 0.25], [0.15, 0.7, 0.15]])

# Perform greedy decoding using tf.raw_ops.log_softmax
logits = tf.raw_ops.LogSoftmax(input=logits)

# Get the indices of the maximum values for each row (greedy decoding)
output = tf.raw_ops.ArgMax(input=logits)

print(output)
