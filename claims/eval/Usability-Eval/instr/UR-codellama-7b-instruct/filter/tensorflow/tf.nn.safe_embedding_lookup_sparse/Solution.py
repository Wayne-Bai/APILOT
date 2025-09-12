
import tensorflow as tf

# Define the lookup function
def lookup_embeddings(ids, embeddings):
    # Use the tensorflow.gather method to retrieve the corresponding embeddings for the ids
    gathered_embeddings = tf.gather(embeddings, ids)
    
    # Check if any of the ids are invalid (i.e., outside of the range of the embedding table)
    num_invalid_ids = tf.size(tf.where(tf.greater(ids, tf.shape(embeddings)[0])[0]))
    
    # If there are any invalid ids, return an empty tensor
    if num_invalid_ids > 0:
        return tf.zeros([num_invalid_ids, tf.shape(gathered_embeddings)[1]], dtype=tf.float32)
    
    # Otherwise, return the gathered embeddings
    else:
        return gathered_embeddings
