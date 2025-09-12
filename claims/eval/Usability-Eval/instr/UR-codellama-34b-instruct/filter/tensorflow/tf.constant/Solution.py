import tensorflow as tf

# Create a tensor-like object
tensor_object = [1, 2, 3, 4, 5]

# Use the `tf.constant` function to create a constant tensor from the tensor-like object
const_tensor = tf.constant(tensor_object)

print(const_tensor) # output: <tf.Tensor 'Const:0' shape=() dtype=int32>
