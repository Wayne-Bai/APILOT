import tensorflow as tf

def transform_elements(elems, fn):
    # Unstack the elements along axis 0
    unstacked_elems = tf.unstack(elems, axis=0)
    
    # Apply the function fn to each unstacked element
    transformed_elems = [fn(elem) for elem in unstacked_elems]
    
    # Stack the transformed elements back together along axis 0
    result = tf.stack(transformed_elems, axis=0)
    
    return result
