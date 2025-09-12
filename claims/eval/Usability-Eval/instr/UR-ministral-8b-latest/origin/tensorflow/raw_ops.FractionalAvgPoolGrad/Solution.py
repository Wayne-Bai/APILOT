import tensorflow as tf

def fractional_avg_pool(input_tensor, window_size):
    batch, height, width, channels = input_tensor.shape
    pooled_height = height // window_size
    pooled_width = width // window_size

    # Creating the empty output tensor
    output_tensor = tf.zeros((batch, pooled_height, pooled_width, channels))

    # Loop over each window to compute the sliding average
    for b in range(batch):
        for h in range(pooled_height):
            for w in range(pooled_width):
                for c in range(channels):
                    # Get the pixels in the current window
                    window_pixels = input_tensor[b, h*window_size:h*window_size+window_size, w*window_size:w*window_size+window_size, c]
                    # Calculate the average for the current window
                    window_average = tf.reduce_mean(window_pixels)
                    # Place the average in the corresponding position in the output
                    output_tensor[b, h, w, c] = window_average

    return output_tensor

# Example usage
input_tensor = tf.random.uniform((2, 16, 16, 3))  # Batch size: 2, Hight: 16, Width: 16, Channels: 3
window_size = 2
output_tensor = fractional_avg_pool(input_tensor, window_size)
print(output_tensor)
