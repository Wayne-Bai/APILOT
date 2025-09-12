
import tensorflow as tf

# Assuming you have already trained your model and have a valid model object named 'model'

# Create a builder object to save the model
builder = tf.saved_model.builder.SavedModelBuilder("/path/to/save/directory")

# Add the model to the builder
builder.add_meta_graph_and_variables(sess=None, tags=[tf.saved_model.tag_constants. serving])

# Save the model
builder.save()
