import tensorflow as tf

def get_subclasses(cls):
    return set(cls.__subclasses__())

def flatten(input):
    return tf.nest.flatten(input)

def pack_sequence_as(structure, flat_sequence):
    return tf.nest.pack_sequence_as(structure, flat_sequence)

def map_structure(func, *structure):
    return tf.nest.map_structure(func, *structure)

def assert_shallow_structure(expected_structure, actual_structure):
    return tf.nest.assert_shallow_structure(expected_structure, actual_structure)

def assert_same_structure(expected_structure, actual_structure, check_types=True):
    return tf.nest.assert_same_structure(expected_structure, actual_structure, check_types=check_types)
