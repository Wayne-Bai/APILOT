import tensorflow as tf

# Initialize a variable
variable = tf.Variable(tf.random.normal([5, 5]))

# Serialize (save) the variable
serialized = tf.saved_model.save(variable, "model_dir")

# Load (deserialize) the variable
loaded_variable = tf.saved_model.load("model_dir").get_tensor("default")

# Check the value of the loaded variable
print(loaded_variable.numpy())
