import tensorflow as tf

# Example data structure
example_data = {
    'example': {
        'id': 42,
        'name': 'test',
        'value': 3.14,
        'labels': ['a', 'b', 'c'],
        'metadata': {
            'element_type': 'float32',
            'partition': 1
        }
    }
}

# Convert the example data into a Tensor
example_tensor = {
    'example': {
        'id': tf.constant(42, dtype=tf.int32),
        'name': tf.constant(b'test', dtype=tf.string),
        'value': tf.constant(3.14, dtype=tf.float32),
        'labels': tf.constant(['a', 'b', 'c'], dtype=tf.string),
        'metadata': {
            'element_type': tf.constant(b'float32', dtype=tf.string),
            'partition': tf.constant(1, dtype=tf.int64)
        }
    }
}

# Serialize the tensor to a binary string
serialized_tensor = example_tensor_raw = ExampleTensor()
example_tensor_raw.ParseFromString(example_tensor)
serialized_tensor_binary = serialized_tensor.SerializeToString()

print(serialized_tensor_binary)
