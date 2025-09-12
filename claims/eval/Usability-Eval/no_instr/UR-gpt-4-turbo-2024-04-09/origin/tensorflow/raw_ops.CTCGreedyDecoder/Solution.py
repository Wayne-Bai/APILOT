import tensorflow as tf

def greedy_decoding(inputs):
    # Assuming 'inputs' is a tensor of logits from a model output
    return tf.argmax(inputs, axis=-1)  # Use argmax to select the maximum logit at each step

# Example logits from a model (e.g. output of an RNN or any neural network)
logits = tf.random.uniform(shape=[10, 5], minval=-1, maxval=1, dtype=tf.float32)  # Example: 10 steps, 5 classes

decoded_output = greedy_decoding(logits)
print(decoded_output)
