import tensorflow as tf

def levenshtein_distance(a, b):
    """
    Computes the (possibly normalized) Levenshtein Edit Distance.
    
    Args:
        a: A string to compare with `b`.
        b: A string to compare with `a`.
    
    Returns:
        The Levenshtein edit distance between `a` and `b`. If the inputs are both empty, 
        returns 0. Otherwise, returns the minimum number of single-character edits (insertions, deletions, or substitutions) needed to transform one string into the other.
    """
    # Initialize the distance matrix with the lengths of a and b.
    distance = np.zeros((len(a) + 1, len(b) + 1))
    
    # Populate the first column of the distance matrix with the length of b.
    for i in range(len(b)):
        distance[0, i] = len(b) - i
    
    # Populate the first row of the distance matrix with the length of a.
    for j in range(len(a)):
        distance[j, 0] = len(a) - j
    
    # Fill in the rest of the distance matrix with the minimum number of edits needed to transform one string into the other.
    for i in range(1, len(b)):
        for j in range(1, len(a)):
            deletion = distance[i - 1, j] + 1
            insertion = distance[i, j - 1] + 1
            substitution = distance[i - 1, j - 1] + (a[j - 1] != b[i])
            distance[i, j] = min(deletion, insertion, substitution)
    
    return distance[-1, -1]
