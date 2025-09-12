import tensorflow as tf

# Define some placeholders for the inputs
x = tf.Variable(0, dtype=tf.float32)
y = tf.Variable(0, dtype=tf.float32)

@tf.function
def compute_operations(a, b):
    # Perform operations
    c = a + b
    d = a * b
    e = tf.math.square(c)
    f = tf.math.sqrt(d)
    return c, d, e, f

# Initialize variables
x.assign(5.0)
y.assign(3.0)

# Execute the function
c_result, d_result, e_result, f_result = compute_operations(x, y)

print("c (a+b) =", c_result.numpy())
print("d (a*b) =", d_result.numpy())
print("e (c^2) =", e_result.numpy())
print("f (sqrt(d)) =", f_result.numpy())
