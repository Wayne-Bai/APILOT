import tensorflow as tf

def levenshtein_distance(s1, s2):
    # Convert strings to tensors
    str1 = tf.constant(list(s1))
    str2 = tf.constant(list(s2))

    # Compute the distance using tf.edit_distance
    distance = tf.edit_distance(str1, str2)

    return distance.numpy()

# Example usage
s1 = "kitten"
s2 = "sitting"
distance = levenshtein_distance(s1, s2)
print("Levenshtein Distance:", distance)
