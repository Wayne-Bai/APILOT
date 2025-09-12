import tensorflow as tf

def tensor_to_strings(tensor):
    return tf.py_function(lambda x: [str(elem.numpy()) for elem in x], [tensor], [tf.string])

tensor = tf.constant([1, 2, 3, 4, 5])
strings = tensor_to_strings(tensor)

print(strings)  # Output: ["1", "2", "3", "4", "5"]
