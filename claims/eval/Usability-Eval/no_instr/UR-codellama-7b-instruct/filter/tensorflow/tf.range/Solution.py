
import tensorflow as tf

# Define a function that takes in a scalar and returns a tensor representing a sequence of numbers
def create_sequence(start):
    # Initialize a new tensor object
    seq = tf.Tensor(shape=(1,), dtype=tf.int32)
    
    # Set the first element of the sequence to the input value
    seq[0] = start
    
    # Define a loop that adds each number in the sequence to itself and stores the result in a new tensor
    for i in range(1, 10):
        seq[i] = seq[i-1] + 1
    
    return seq

# Use the function to create a sequence of numbers starting at 5
start_val = 5
seq = create_sequence(start)

print(seq.numpy())
