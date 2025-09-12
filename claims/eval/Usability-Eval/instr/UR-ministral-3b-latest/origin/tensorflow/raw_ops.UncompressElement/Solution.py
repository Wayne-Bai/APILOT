from tensorflow import raw_ops

def uncompress_dataset(compressed_data):
    uncompressed_data = raw_ops.Uncompress(CompressedDatasetElement(compressed_data))
    return uncompressed_data

# Sample compressed data tensor
compressed_data = tf.constant([[1, 2], [3, 4]], dtype=tf.int32)

# Call the uncompress function
uncompressed_data = uncompress_dataset(compressed_data)
print(uncompressed_data)
