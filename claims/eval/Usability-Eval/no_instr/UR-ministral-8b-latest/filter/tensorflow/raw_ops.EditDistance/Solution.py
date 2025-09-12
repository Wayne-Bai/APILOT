import tensorflow as tf

def levenshtein_distance(a, b):
    a = a[:]
    b = b[:]
    if len(a) < len(b):
        return levenshtein_distance(b, a)

    if len(b) == 0:
        return len(a)

    previous_row = range(len(b) + 1)
    for i, c1 in enumerate(a):
        current_row = [i + 1]
        for j, c2 in enumerate(b):
            substitutions = previous_row[j + 1] + 1
            insertions = current_row[j] + 1
            deletions = previous_row[j] + 1

            if c1 == c2:
                current_row.append(min(substitutions, insertions, deletions))
            else:
                current_row.append(min(substitutions, insertions, deletions))

        previous_row = current_row

    return previous_row[-1]

# Example usage
a = "kitten"
b = "sitting"
print("Levenshtein Distance:", levenshtein_distance(a, b))
