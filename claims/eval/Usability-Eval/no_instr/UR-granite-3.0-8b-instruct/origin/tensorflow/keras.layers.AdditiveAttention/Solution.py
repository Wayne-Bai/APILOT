import tensorflow as tf

def create_attention_mechanism(num_units, memory, num_heads=1, name=None):
    with tf.name_scope(name, default_name="additive_attention"):
        # Create a linear transformation of the inputs
        query = tf.layers.dense(memory, num_units, activation=tf.tanh, name="query")
        key = tf.layers.dense(memory, num_units, activation=tf.tanh, name="key")
        value = tf.layers.dense(memory, num_units, activation=None, name="value")

        # Create the attention scores
        attention_scores = tf.nn.softmax(
            tf.matmul(query, tf.transpose(key, [0, 2, 1])), axis=-1)

        # Create the context vector
        context = tf.matmul(attention_scores, value)

        return context

# Example usage:
num_units = 128
memory = tf.random.normal([10, 32, 128])  # Batch size, sequence length, num_units
context = create_attention_mechanism(num_units, memory)
