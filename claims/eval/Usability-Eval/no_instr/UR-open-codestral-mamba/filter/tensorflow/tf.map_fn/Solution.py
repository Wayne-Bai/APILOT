import tensorflow as tf

def transform_elements(tensor, fn):
    # Determine the size of axis 0
    size = tf.shape(tensor)[0]

    # We need to unstack and then stack the tensor.
    outputs = []
    for i in range(size):
        # Use tf.gather to pick out the desired element at each iteration
        element = tf.gather(tensor, i)
        outputs.append(fn(element))
    return tf.stack(outputs)

# Here's an example usage:
def multiply_by_two(tensor):
    return tensor * 2

tensor = tf.constant([1, 2, 3, 4])
result = transform_elements(tensor, multiply_by_two)
print(result)
