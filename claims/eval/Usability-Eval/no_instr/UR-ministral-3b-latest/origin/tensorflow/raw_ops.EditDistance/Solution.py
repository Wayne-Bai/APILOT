import tensorflow as tf

def levenshtein_distance(setting1, setting2):
    dist = tf.raw_ops.levenshtein_distance()
    dist = dist(setting1, setting2)
    return dist

# Test the function
string1 = tf.constant('kitten', tf.string)
string2 = tf.constant('sitting', tf.string)
distance = levenshtein_distance(string1, string2)
print(distance)
