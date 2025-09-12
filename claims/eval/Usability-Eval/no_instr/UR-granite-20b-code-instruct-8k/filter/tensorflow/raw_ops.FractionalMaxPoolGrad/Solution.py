import tensorflow as tf

# Input tensor
input_tensor = tf.constant([[[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]], [[7.0, 8.0, 9.0], [10.0, 11.0, 12.0]]])

#pooling_ratio
pooling_ratio = [1.0, 1.0, 1.0]

#pooling_type
pooling_type = "MAX"

#pseudo_grad_fn
pseudo_grad_fn = "pseudo_grad_fn"

# overlapping
overlapping = False

#Input arguments
inputs = [input_tensor, pooling_ratio, pooling_type, pseudo_grad_fn, overlapping]

#Output of FractionalMaxPoolGrad function
output = tf.raw_ops.FractionalMaxPoolGrad(inputs=inputs)

print(output)
