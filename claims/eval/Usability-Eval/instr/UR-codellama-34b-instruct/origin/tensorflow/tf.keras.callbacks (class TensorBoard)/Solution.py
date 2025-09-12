
import tensorflow as tf

# Create a summary writer
writer = tf.summary.FileWriter('logs')

# Create a summary for a tensor
tensor_summary = tf.summary.TensorSummary(name='my_tensor', data=tf.Variable(tf.zeros((3, 2))), step=0)

# Write the summary to the file
writer.add_summary(tensor_summary)

# Close the writer
writer.close()
