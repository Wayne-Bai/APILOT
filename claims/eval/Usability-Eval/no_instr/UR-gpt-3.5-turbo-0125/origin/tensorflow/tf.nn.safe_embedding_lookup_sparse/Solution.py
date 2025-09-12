
import tensorflow as tf

def lookup_embedding(embedding_matrix, ids):
    # Define placeholder for input IDs
    input_ids = tf.placeholder(shape=[None], dtype=tf.int32)
    
    # Lookup embedding vectors for input IDs
    embed_lookup = tf.nn.embedding_lookup(embedding_matrix, input_ids)
    
    # Handling invalid IDs using tf.where and tf.reduce_any
    valid_ids_mask = tf.not_equal(input_ids, -1)
    valid_ids = tf.where(valid_ids_mask)
    valid_embeddings = tf.gather(embed_lookup, valid_ids)
    
    # Handling empty features using tf.where and tf.reduce_any
    empty_features_mask = tf.reduce_any(valid_embeddings, axis=1)
    non_empty_embeddings = tf.boolean_mask(valid_embeddings, empty_features_mask)
    
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        result = sess.run(non_empty_embeddings, feed_dict={input_ids: ids})
    
    return result
