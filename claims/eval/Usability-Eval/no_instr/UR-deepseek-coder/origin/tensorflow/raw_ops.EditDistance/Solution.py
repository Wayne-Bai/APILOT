import tensorflow as tf

def levenshtein_distance(s1, s2, normalize=False):
    # Convert input strings to tensors
    s1_tensor = tf.convert_to_tensor(s1, dtype=tf.string)
    s2_tensor = tf.convert_to_tensor(s2, dtype=tf.string)

    # Compute the Levenshtein distance
    distance = tf.edit_distance(
        tf.SparseTensor(indices=[[0, 0]], values=s1_tensor, dense_shape=[1, 1]),
        tf.SparseTensor(indices=[[0, 0]], values=s2_tensor, dense_shape=[1, 1]),
        normalize=normalize
    )

    return distance

# Example usage:
s1 = "kitten"
s2 = "sitting"
distance = levenshtein_distance(s1, s2, normalize=True)
print(distance.numpy())
