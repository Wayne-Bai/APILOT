import tensorflow as tf

# Initialize DTensor
tf.experimental.dtensor.initialize()

# Optionally, set the communication fabric here
# Note: Adjust the configuration according to your specific setup
tf.experimental.dtensor.set_communication_fabric('your_fabric_here')

# Verify the initialization
print("DTensor initialized successfully.")
