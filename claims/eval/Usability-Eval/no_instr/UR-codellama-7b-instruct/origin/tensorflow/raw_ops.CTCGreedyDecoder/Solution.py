
import tensorflow as tf

def greedy_decode(logits):
    """Performs greedy decoding on the logits given in inputs."""
    # Step 1: Get the most likely token index for each timestep
    topk = tf.nn.topk(logits, k=1)
    indices = topk.indices[:, -1]  # get the last index of each timestep

    # Step 2: Use the most likely token index to calculate the final output
    tokens = tf.gather_nd(inputs=logits, indices=indices)

    return tokens
