import tensorflow as tf

def fractional_average_pooling(input_tensor, pooling_ratio):
    # Perform fractional average pooling
    pooled_output = tf.raw_ops.FractionalAvgPool(value=input_tensor, 
                                                  pool_size=pooling_ratio)
    return pooled_output

# Example usage
if __name__ == "__main__":
    input_tensor = tf.random.uniform((1, 4, 4, 1))  # Example input tensor
    pooling_ratio = [2.0, 2.0]  # Example pooling ratio
    result = fractional_average_pooling(input_tensor, pooling_ratio)
    print(result)
