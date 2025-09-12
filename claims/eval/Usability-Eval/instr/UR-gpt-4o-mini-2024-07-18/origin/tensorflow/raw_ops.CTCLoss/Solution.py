import tensorflow as tf

def compute_ctc_loss(logits, labels, label_length, logit_length):
    # Compute CTC Loss
    loss = tf.nn.ctc_loss(
        labels=labels,
        inputs=logits,
        sequence_length=logit_length,
        time_major=False
    )
    return loss

# Example usage
if __name__ == "__main__":
    # Sample data
    logits = tf.constant([[0.1, 0.2, 0.7], 
                          [0.3, 0.4, 0.3]], dtype=tf.float32)  # Shape: [2, 3]
    labels = tf.convert_to_tensor([[1], [2]], dtype=tf.int32)  # Shape: [2, 1]
    label_length = tf.constant([1, 1], dtype=tf.int32)  # Length of each label
    logit_length = tf.constant([2, 2], dtype=tf.int32)  # Length of each logit sequence

    loss = compute_ctc_loss(logits, labels, label_length, logit_length)
    print("CTC Loss:", loss.numpy())
