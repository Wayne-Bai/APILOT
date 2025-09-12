import numpy as np
from scipy.ndimage import generic_filter

# Define a function to perform the filtering
def uniformity_filter(roll_window, image):
    def uniform_filter_patch(patch):
        return np.mean(patch)  # Implementing a simple mean filter as an example

    return generic_filter(image, uniform_filter_patch, size=roll_window)

# Example usage
if __name__ == "__main__":
    # Create a sample 2D image with random values
    image = np.random.rand(10, 10)

    # Define the roll window size
    roll_window = (3, 3)

    # Apply the filter
    filtered_image = uniformity_filter(roll_window, image)

    # Print the original and filtered images
    print("Original Image:\n", image)
    print("\nFiltered Image:\n", filtered_image)
