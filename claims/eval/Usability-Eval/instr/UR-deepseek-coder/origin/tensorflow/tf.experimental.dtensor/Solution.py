import tensorflow as tf

# Define a simple function to demonstrate the usage of the experimental.dtensor namespace
def example_dtensor_function():
    # Create a simple DTensor
    dtensor = tf.experimental.dtensor.DTensor(
        shape=[2, 2],
        dtype=tf.float32,
        layout=tf.experimental.dtensor.Layout.replicated(2)
    )
    
    # Perform some operations on the DTensor
    result = dtensor + dtensor
    
    return result

# Example usage
if __name__ == "__main__":
    output = example_dtensor_function()
    print(output)
