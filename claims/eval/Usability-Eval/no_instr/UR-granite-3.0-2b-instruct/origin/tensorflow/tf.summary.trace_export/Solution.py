import tensorflow as tf

# Assuming 'tr' is the active trace
tr.stop()

# Export the active trace as a Summary file
tf.summary.write('path/to/summary')

# Export the active trace as a Profile file
tf.profile.write('path/to/profile')
