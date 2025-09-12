import tensorflow as tf

# Create a sparse tensor
indices = [[0, 0], [1, 0], [1, 3], [3, 0]]
values = [0, 1, 2, 3]
dense_shape = [4, 4]
spr = tf.sparse.SparseTensor(indices, values, dense_shape)

# Split the sparse tensor into 2 tensors along dimension 0
num_split = 2
sparse_tensor_list = tf.sparse.split(spr, num_split, axis=0)

# Initialize the session
with tf.Session() as sess:
    # Run the session
    result = sess.run(sparse_tensor_list)

# Print the result
for i, sp in enumerate(result):
    print(f"SparseTensor {i + 1}:")
    print(tf.sparse.to_dense(sp).eval())
    print("\n")
