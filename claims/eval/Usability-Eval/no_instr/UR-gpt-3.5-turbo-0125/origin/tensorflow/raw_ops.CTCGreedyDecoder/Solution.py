
import tensorflow as tf

logits = tf.constant([[1.2, 0.5, 2.1], [2.5, 1.3, 0.7]])  # Example logits tensor
decoded_sequence, scores = tf.raw_ops.CTCGreedyDecoder(inputs=logits, sequence_length=[2, 3])

with tf.Session() as sess:
    decoded_sequence_result, scores_result = sess.run([decoded_sequence, scores])
    print("Decoded sequence:", decoded_sequence_result)
    print("Scores:", scores_result)
