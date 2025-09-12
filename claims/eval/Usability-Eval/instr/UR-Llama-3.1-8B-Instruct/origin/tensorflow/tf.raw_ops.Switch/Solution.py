# Importing necessary libraries
import tensorflow as tf

# Creating a simple TensorFlow graph
with tf.Graph().as_default():
    # Defining the input tensors
    input_tensor = tf.constant([[1, 2], [3, 4]])
    
    # Defining the prediction (determined by pred, assume it's 1 for now)
    pred = tf.constant(1)
    
    # Defining the function to forward data to the output port determined by pred
    @tf.function
    def forward_data(input_tensor, pred):
        # Assuming we have a conditioning function that determines which output port to use based on the pred value
        def condition(x):
            return x >= 5
        
        # Using the tf.cond function to forward data to the output port determined by pred
        result = tf.cond(pred == 1,
                        lambda: tf.identity(input_tensor),  # If pred is 1, return the input tensor
                        lambda: tf.add(input_tensor, 1))  # If pred is not 1, add 1 to the input tensor
        return result
    
    # Running the forward_data function with the input_tensor and pred
    result = forward_data(input_tensor, pred)
    
    # Printing the result
    print(result)

