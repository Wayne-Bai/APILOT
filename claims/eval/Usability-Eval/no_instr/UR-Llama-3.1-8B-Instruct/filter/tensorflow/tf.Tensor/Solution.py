# Import the necessary libraries from tensorflow
import tensorflow as tf

# Define a function to create a multi-dimensional array
def create_multidimensional_array():
    """
    Creates a multi-dimensional array using tensorflow.
    
    Returns:
        A tensorflow tensor representing a multi-dimensional array.
    """
    # Define the shape of the array
    shape = (2, 3, 4)
    
    # Create the array with random values between 0 and 1
    array = tf.random.uniform(shape, dtype=tf.float32)
    
    return array

# Create a multi-dimensional array
array = create_multidimensional_array()

# Print the array
print("Multi-dimensional Array:")
print(array)

# Shape of the array
print("\nShape of the array:")
print(array.shape)

# Size of the array
print("\nSize of the array:")
print(array.size)

# Rank of the array (number of dimensions)
print("\nRank of the array:")
print(array.rank)
