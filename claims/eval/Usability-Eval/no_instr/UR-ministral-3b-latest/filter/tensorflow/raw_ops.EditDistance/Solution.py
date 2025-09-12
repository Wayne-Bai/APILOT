import tensorflow as tf

def levenshtein_edit_distance(text1, text2):
    # Adding an extra element to the text for alignment
    text1 = [0] + list(text1)
    text2 = [0] + list(text2)

    m = len(text1)
    n = len(text2)

    # Initialize a matrix to hold the distances
    dist = tf.zeros([m + 1, n + 1], dtype=tf.int32)

    # Fill in the leftmost column of the matrix
    for i in range(1, m + 1):
        dist[i, 0] = i

    # Fill in the topmost row of the matrix
    for j in range(1, n + 1):
        dist[0, j] = j

    # Fill in the rest of the matrix using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cost = tf.cast(text2[j - 1] == text1[i - 1], dtype=tf.float32)
            dist[i, j] = tf.minimum(
                dist[i - 1, j] + 1,       # Deletion
                dist[i, j - 1] + 1,       # Insertion
                dist[i - 1, j - 1] * (1 - cost) + 1 - cost * 2  # Substitution
            )

    return dist[-1, -1]

# Example usage:
text1 = "kitten"
text2 = "sitting"

distance = levenshtein_edit_distance(text1, text2)
print(f"The Levenshtein Edit Distance between '{text1}' and '{text2}' is {distance}")
