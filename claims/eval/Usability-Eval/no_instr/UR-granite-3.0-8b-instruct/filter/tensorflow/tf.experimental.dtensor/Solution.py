import tensorflow as tf

class DTensorAPI:
    def __init__(self):
        self.dtensor = tf.experimental.dtensor

    def create_dtensor(self, data):
        """
        Create a dtensor from a numpy array.

        Args:
            data (numpy.ndarray): The data to create the dtensor from.

        Returns:
            tf.experimental.dtensor.DTensor: The created dtensor.
        """
        return self.dtensor.from_numpy(data)

    def to_numpy(self, dtensor):
        """
        Convert a dtensor to a numpy array.

        Args:
            dtensor (tf.experimental.dtensor.DTensor): The dtensor to convert.

        Returns:
            numpy.ndarray: The converted numpy array.
        """
        return dtensor.to_numpy()
