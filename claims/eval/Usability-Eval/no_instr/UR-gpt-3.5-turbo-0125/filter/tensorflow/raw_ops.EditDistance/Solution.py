
import tensorflow as tf

string1 = tf.constant("kitten")
string2 = tf.constant("sitting")

distance = tf.edit_distance(tf.reshape(string1, [1, -1]), tf.reshape(string2, [1, -1]), normalize=True)

with tf.Session() as sess:
    result = sess.run(distance)
    print("Normalized Levenshtein Edit Distance:", result)
