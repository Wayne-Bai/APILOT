import tensorflow as tf

def gather_slices_from_var(variable, indices):
    gather_elem = tf.raw_ops.StableGatherSlices(select_slices=True)
    gather_elem.gather_variable = variable
    gather_elem.indices = indices
    return gather_elem

# Sample usage
variable = tf.Variable([1, 2, 3, 4, 5])
indices = tf.constant([1, 3])

output = gather_slices_from_var(variable, indices)
print(output.numpy())  # This will output [2, 4]
