import tensorflow as tf

# Assuming params and indices are already defined
# params shape: [batch_size, max_length, embedding_size]
# indices shape: [batch_size, max_length]

# Flatten the params tensor along the first two dimensions
params_flattened = tf.reshape(params, [-1, params.shape[-1]])

# Gather ragged slices from params axis 0 according to indices
gathered = tf.gather(params_flattened, indices)

# Reshape the gathered tensor to match the original shape
gathered_reshaped = tf.reshape(gathered, [-1, params.shape[1], params.shape[-1]])
