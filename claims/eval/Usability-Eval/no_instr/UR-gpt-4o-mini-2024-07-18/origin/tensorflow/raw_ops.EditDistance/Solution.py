import tensorflow as tf

def levenshtein_distance(str1, str2):
    # Convert the input strings to tensors
    input1 = tf.constant([str1])
    input2 = tf.constant([str2])
    
    # Compute the Levenshtein distance using tf.edit_distance
    distance = tf.edit_distance(input1, input2, normalize=False)
    
    return distance.numpy()[0]

# Example usage
str1 = "kitten"
str2 = "sitting"
distance = levenshtein_distance(str1, str2)
print(f"The Levenshtein distance between '{str1}' and '{str2}' is: {distance}")
