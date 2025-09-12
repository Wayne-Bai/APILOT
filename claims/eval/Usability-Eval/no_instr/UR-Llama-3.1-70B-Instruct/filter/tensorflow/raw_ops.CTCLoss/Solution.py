# Import necessary libraries
import tensorflow as tf
from tensorflow.keras import backend as K
import numpy as np

# Define input parameters
# labels: A SparseTensor. labels indices must be in descending order.
# logits: A Tensor. The logits are the output of the neural network.
# logit_length: An int32 Tensor. The length of the logits sequence.
# label_length: An int32 Tensor. The length of the labels sequence.

# Define the function
def ctc_loss(labels, logits, logit_length, label_length):
    # Convert logits to float32 (to match with tf.nn.ctc_loss requirements)
    logits = tf.cast(logits, tf.float32)
    
    # Calculate the CTC Loss
    ctc_loss_value = tf.nn.ctc_loss(labels, logits, label_length, logit_length)
    
    # Return the mean CTC Loss
    return tf.reduce_mean(ctc_loss_value)

# Example usage
if __name__ == "__main__":
    # Define the input parameters
    labels = tf.SparseTensor(indices=[[0, 0], [1, 0]], values=[1, 2], dense_shape=[2, 2])
    logits = np.array([[[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8]], [[0.9, 0.10, 0.11, 0.12], [0.13, 0.14, 0.15, 0.16]]])
    logit_length = 2
    label_length = 2
    
    # Calculate the CTC Loss
    loss_value = ctc_loss(labels, logits, logit_length, label_length)
    
    print("CTC Loss: ", loss_value)
