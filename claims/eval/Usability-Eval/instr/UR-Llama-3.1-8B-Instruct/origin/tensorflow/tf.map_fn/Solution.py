import tensorflow as tf

def unstack_and_apply(elems, fn):
    """
    Transforms elems by applying fn to each element unstacked on axis 0.
    
    Args:
        elems: The input tensor.
        fn: The function to apply to each element.
        
    Returns:
        A tensor with the same shape as elems, but with the function applied to each element.
    """
    
    # Use tensor_unstack to split elems along axis 0
    unstacked_elems = tf.unstack(elems, axis=0)
    
    # Apply the function fn to each element in the unstacked elems
    transformed_elems = tf.map_fn(fn, unstacked_elems, dtype=elems.dtype)
    
    # Use tensor_stack to stack the transformed elems back together along axis 0
    transformed_elems = tf.stack(transformed_elems, axis=0)
    
    return transformed_elems

# Example usage:
if __name__ == "__main__":
    # Create a sample tensor
    elems = tf.constant([[1, 2, 3], [4, 5, 6]], dtype=tf.float32)
    
    # Apply a function to each element (in this case, doubling the value)
    def fn(x):
        return x * 2
    
    transformed_elems = unstack_and_apply(elems, fn)
    
    # Print the result
    print(transformed_elems)
