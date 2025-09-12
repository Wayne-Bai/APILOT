import tensorflow as tf

def uncompress_dataset_element(compressed_tensors, shapes, types):
    """
    Uncompresses a compressed dataset element.

    Args:
    - compressed_tensors: A list of tensors representing the compressed dataset element.
    - shapes: A list of `tf.TensorShape` representing the shapes of the uncompressed elements.
    - types: A list of `tf.DType` representing the types of the uncompressed elements.

    Returns:
    - A list of uncompressed tensors.
    """
    # Create a tensor spec for each element using its shape and dtype
    specs = [tf.TensorSpec(shape, dtype) for shape, dtype in zip(shapes, types)]

    # Use tf.raw_ops.UncompressElement to uncompress the dataset element
    uncompressed_elements = tf.raw_ops.UncompressElement(
        input=compressed_tensors,
        output_shapes=shapes,
        output_types=types
    )

    # Each uncompressed element will match the corresponding spec
    return [tf.convert_to_tensor(elem, spec.dtype) for elem, spec in zip(uncompressed_elements, specs)]

# Example usage:
compressed_element = [
    tf.constant(b'compressed_tensor_1'),
    tf.constant(b'compressed_tensor_2')
]

shapes = [
    tf.TensorShape([10, 10]),
    tf.TensorShape([5, 5])
]

types = [
    tf.float32,
    tf.int32
]

uncompressed = uncompress_dataset_element(compressed_element, shapes, types)
print(uncompressed)
