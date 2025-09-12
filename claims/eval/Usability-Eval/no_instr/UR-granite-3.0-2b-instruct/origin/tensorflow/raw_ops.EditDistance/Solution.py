import tensorflow as tf

def levenshtein_distance(s, t):
    m, n = len(s), len(t)
    d = tf.zeros([m + 1, n + 1], dtype=tf.int32)

    for i in range(m + 1):
        d[i, 0] = i
    for j in range(n + 1):
        d[0, j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i, j] = tf.minimum(
                d[i - 1, j] + 1,  # Deletion
                d[i, j - 1] + 1,  # Insertion
                d[i - 1, j - 1] + cost  # Substitution
            )

    return d[m, n]

# Example usage:
s = tf.constant("kitten")
t = tf.constant("sitting")
distance = levenshtein_distance(s, t)
print(f"The Levenshtein distance between '{s.numpy()}' and '{t.numpy()}' is {distance.numpy()}")
