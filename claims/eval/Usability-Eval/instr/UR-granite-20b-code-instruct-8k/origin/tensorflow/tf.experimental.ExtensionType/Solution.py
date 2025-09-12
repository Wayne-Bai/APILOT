import tensorflow as tf

class ExtensionTypeBase(tf.ExtensionType):
    def __init__(self, data):
        self.data = data

    def process_data(self):
        # Add your data processing logic here
        pass
