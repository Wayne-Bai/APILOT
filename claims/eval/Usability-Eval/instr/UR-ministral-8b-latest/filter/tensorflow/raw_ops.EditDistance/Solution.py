import tensorflow as tf

def levenshtein_distance(s1, s2):
    m = len(s1)
    n = len(s2)

    # Create a distance matrix
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the matrix with base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the distance matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,  # deletion
                               dp[i][j - 1] + 1,  # insertion
                               dp[i - 1][j - 1] + 1)  # substitution

    # The Levenshtein distance is the bottom-right corner of the matrix
    return dp[m][n]

# Example usage
str1 = "kitten"
str2 = "sitting"
print(f"Levenshtein distance between '{str1}' and '{str2}': {levenshtein_distance(str1, str2)}")
