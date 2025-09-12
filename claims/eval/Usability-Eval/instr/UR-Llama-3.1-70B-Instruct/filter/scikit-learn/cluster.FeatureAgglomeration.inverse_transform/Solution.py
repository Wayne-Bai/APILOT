# Importing necessary libraries
from sklearn.preprocessing import StandardScaler
import numpy as np

class InverseTransformer:
    def __init__(self, n_features):
        self.n_features = n_features
        self.scaler = StandardScaler()

    def transform(self, data):
        """
        Scale the data using StandardScaler.

        Args:
            data (array-like): Data to be scaled.

        Returns:
            scaled_data (array-like): Scaled data.
        """
        scaled_data = self.scaler.fit_transform(data)
        return scaled_data

    def inverse_transform(self, scaled_data):
        """
        Inverse the transformation and return a vector of size n_features.

        Args:
            scaled_data (array-like): Data to be inverse transformed.

        Returns:
            inverted_data (array-like): Inverse transformed data.
        """
        inverted_data = self.scaler.inverse_transform(scaled_data)
        return inverted_data


# Example usage
if __name__ == "__main__":
    n_features = 5
    transformer = InverseTransformer(n_features)

    # Generate random data
    np.random.seed(0)
    data = np.random.rand(10, n_features)

    # Transform the data
    scaled_data = transformer.transform(data)

    # Inverse transform the data
    inverted_data = transformer.inverse_transform(scaled_data)

    # Check if the original data and inverted data are the same
    np.testing.assert_almost_equal(data, inverted_data)
    print("Original data and inverted data are the same.")
