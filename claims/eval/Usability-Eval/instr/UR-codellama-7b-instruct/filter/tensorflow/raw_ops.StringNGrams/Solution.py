
import tensorflow as tf

# Define a function to create ngrams from ragged string data
def create_ngrams(data):
    # Split the input data into individual strings
    split_data = tf.strings.split(data)
    
    # Flatten the list of splits into a 1D tensor
    flattened_data = tf.reshape(split_data, [-1])
    
    # Define the window size for ngrams
    window_size = 3
    
    # Define the stride for ngrams
    stride = 1
    
    # Create a sliding window over the flattened data with the defined window size and stride
    slices = tf.range(window_size, tf.shape(flattened_data)[0], stride)
    
    # Use the sliding window to extract ngrams from the flattened data
    ngrams = [tf.gather(flattened_data, s) for s in slices]
    
    # Return the list of ngrams as a tensor
    return tf.concat(ngrams, axis=0)
