import tensorflow as tf

# Set the value of the parameter to start background threads of asynchronous transformations upon iterator creation
tf.data.experimental.AUgmentationDataset.options().deterministic = False
