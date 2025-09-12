import tensorflow as tf

def levenshtein_distance(a, b):
    # Initialize the distance matrix with a row of zeros for each string
    d = [[0] * (len(b) + 1)]
    for i in range(len(a)):
        # Add a new row to the distance matrix for each character in the first string
        d.append([i+1] + [0] * len(b))
    for j in range(len(b)):
        # Compute the edit distance for each character in the second string
        for i in range(len(a)):
            # If the characters match, the distance is 0
            if a[i] == b[j]:
                d[i][j+1] = 0
            else:
                # Otherwise, the distance is the minimum of the previous character's distance plus 1, or the previous row's distance plus 1
                d[i][j+1] = min(d[i-1][j+1] + 1, d[i][j] + 1)
    return d[-1][-1]
