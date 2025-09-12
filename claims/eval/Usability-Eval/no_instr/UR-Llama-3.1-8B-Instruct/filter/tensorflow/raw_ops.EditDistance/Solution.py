import tensorflow as tf

# Define a function to compute the Levenshtein edit distance
def levenshtein_distance(x, y):
    """Computes the Levenshtein edit distance between two sequences x and y"""
    
    # Initialize the distance matrix
    distances = tf.fill([len(x) + 1, len(y) + 1], 0)
    
    # Initialize the first row and column of the distance matrix
    distances = tf.tensor_scatter_nd_update(distances, [[0, 0]], [0])
    for i in range(1, len(x) + 1):
        distances = tf.tensor_scatter_nd_update(distances, [[i, 0]], [i])
    for j in range(1, len(y) + 1):
        distances = tf.tensor_scatter_nd_update(distances, [[0, j]], [j])
    
    # Fill in the rest of the distance matrix
    for i in range(1, len(x) + 1):
        for j in range(1, len(y) + 1):
            if x[i - 1] == y[j - 1]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            
            distances[i, j] = tf.math.minimum(
                tf.math.minimum(
                    distances[i - 1, j] + 1,
                    distances[i, j - 1] + 1
                ),
                distances[i - 1, j - 1] + substitution_cost
            )
    
    # Return the distance between the two sequences
    return distances[-1, -1]

# Test the function
sequence1 = tf.constant(["abc", "def"])
sequence2 = tf.constant(["axc", "dvf"])
distance = levenshtein_distance(sequence1, sequence2)
print(distance)
