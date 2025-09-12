
import tensorflow as tf

input_structure = {
    'a': tf.constant(1),
    'b': {
        'c': tf.constant(2),
        'd': tf.constant(3)
    }
}

flat_list = tf.nest.flatten(input_structure)
print(flat_list)

nested_structure = tf.nest.pack_sequence_as(input_structure, flat_list)
print(nested_structure)
