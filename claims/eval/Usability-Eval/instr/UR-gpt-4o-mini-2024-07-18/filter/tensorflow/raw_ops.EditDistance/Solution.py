import tensorflow as tf

def compute_levenshtein_distance(s1, s2):
    # Creating TensorFlow constants from the input strings
    str1 = tf.constant(s1)
    str2 = tf.constant(s2)

    # Using tf.strings.to_hash_bucket to create a numerical representation
    hashed_s1 = tf.strings.to_hash_bucket(str1, num_buckets=2**24)
    hashed_s2 = tf.strings.to_hash_bucket(str2, num_buckets=2**24)

    # Computing Levenshtein distance (using tf.edit_distance)
    distance = tf.edit_distance(tf.expand_dims(hashed_s1, 0), tf.expand_dims(hashed_s2, 0), normalize=False)

    return distance.numpy()[0]  # Returning the distance as a scalar

# Example usage
distance = compute_levenshtein_distance("kitten", "sitting")
print("Levenshtein Distance:", distance)
