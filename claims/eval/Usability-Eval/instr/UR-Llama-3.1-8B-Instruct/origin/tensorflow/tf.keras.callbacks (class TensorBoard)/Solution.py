# Import necessary libraries
import tensorflow as tf
from tensorflow.keras.callbacks import TensorBoard

# Create a TensorBoard callback object with the name of the log directory
tensorboard_callback = TensorBoard(
    log_dir='./logs',  # Specify the log directory
    histogram_freq=1,  # Set the frequency at which histograms are written
    write_graph=True,  # Specify whether to write the graph
    write_images=True  # Specify whether to include images in the log
)

#... (rest of the code remains the same as in your previous code)
