# Import necessary libraries
import tensorflow as tf

# Define the CTC Loss function based on tf.raw_ops.ctc_loss
def ctc_loss(predicted_log_probs, label_lengths, label_ids, label_weights=None):
    """
    Calculate the CTC Loss (log probability) for each batch entry.
    
    Args:
    - predicted_log_probs: A 2D Tensor of shape [time_steps, batch_size] or [batch_size, time_steps]
      with log probabilities of each label at each time step.
    - label_lengths: A 1D Tensor of shape [batch_size] with the number of labels in each batch entry.
    - label_ids: A 1D Tensor of shape [batch_size] with the actual label IDs for each batch entry.
    - label_weights: Optional: A 1D Tensor of shape [batch_size] with the weights for each label.
    
    Returns:
    - loss: A 1D Tensor of shape [batch_size] with the CTC Loss (log probability) for each batch entry.
    """
    # Reshape the predicted log probabilities to [time_steps, batch_size]
    predicted_log_probs = tf.transpose(predicted_log_probs, [1, 0])
    
    # Use the tf.raw_ops.ctc_loss function to calculate the CTC Loss
    # This function requires the predicted log probabilities, the label lengths, and the label IDs
    cost = tf.raw_ops.CtcLoss(predicted_log_probs, label_lengths, label_ids, label_weights)
    
    # Reshape the cost to a 1D Tensor (per batch entry)
    loss = tf.reshape(cost, [-1])
    
    return loss
