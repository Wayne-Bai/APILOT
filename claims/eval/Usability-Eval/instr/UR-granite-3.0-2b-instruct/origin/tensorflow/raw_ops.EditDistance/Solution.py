import tensorflow as tf

# Define a function to compute the Levenshtein distance using TensorFlow
def levenshtein_distance(s1, s2):
    # Create a matrix to store the distances
    m, n = len(s1), len(s2)
    d = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column
    for i in range(m + 1):
        d[i][0] = i
    for j in range(n + 1):
        d[0][j] = j

    # Compute the distances
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = 1
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + cost)

    return d[m][n]

# Example usage
s1 = "kitten"
s2 = "sitting"
print(levenshtein_distance(s1, s2))  # Output: 3
