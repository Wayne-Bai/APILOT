import tensorflow as tf

def compute_levenshtein_distance(source, target, normalize=False):
    # Converts the inputs to SparseTensor
    source_sp_tensor = tf.strings.unicode_decode(source, "UTF-8")
    source_sp_tensor = tf.sparse.SparseTensor(
        indices=[[i, 0] for i in range(tf.size(source_sp_tensor))],
        values=source_sp_tensor,
        dense_shape=[tf.size(source_sp_tensor), 1]
    )
    
    target_sp_tensor = tf.strings.unicode_decode(target, "UTF-8")
    target_sp_tensor = tf.sparse.SparseTensor(
        indices=[[i, 0] for i in range(tf.size(target_sp_tensor))],
        values=target_sp_tensor,
        dense_shape=[tf.size(target_sp_tensor), 1]
    )

    # Calculate the edit distance
    edit_distance = tf.raw_ops.EditDistance(
        hypothesis=source_sp_tensor,
        truth=target_sp_tensor,
        normalize=normalize
    )
    
    return edit_distance

# Example usage
source = tf.constant(['kitten'])
target = tf.constant(['sitting'])
distance = compute_levenshtein_distance(source, target)
print('Levenshtein Edit Distance:', distance.numpy())
