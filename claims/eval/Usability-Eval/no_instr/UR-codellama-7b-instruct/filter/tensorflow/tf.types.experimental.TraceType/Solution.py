
import tensorflow as tf

class MyObject:
    def __init__(self, data):
        self.data = data
    
    @tf.function
    def process_data(self):
        # Perform some computation on self.data using TensorFlow APIs
        ...
