import tensorflow as tf

@tf.function
def levenshtein_distance(str1, str2):
    if str1 == str2:
        return 0
    vec = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            possible = [vec[i-1][j]+1, vec[i][j-1]+1, vec[i-1][j-1]+(not str1[i-1]==str2[j-1])]
            vec[i][j] = min(possible)
    return vec[len(str1)][len(str2)]

# Example usage
str1 = "dragon"
str2 = "dark"
distance = levenshtein_distance(str1, str2)
print(distance)
