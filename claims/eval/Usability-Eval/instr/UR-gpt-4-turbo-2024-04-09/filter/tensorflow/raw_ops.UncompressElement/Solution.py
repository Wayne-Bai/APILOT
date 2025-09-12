import tensorflow as tf

# Assuming tensorflow_io provides the necessary API
from tensorflow_io import experimental as tfio_exp

def decompress_dataset_element(compressed_element):
    # Use tensorflow_io.experimental to decompress dataset element
    decompressed_element = tfio_exp.uncompress(compressed_element)
    return decompressed_element
