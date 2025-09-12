# Import necessary libraries
from sklearn.metrics.pairwise import manhattan_distances

# Function to compute L1 distances between vectors in X and Y
def compute_l1_distances(X, Y):
    # Compute L1 distances
    distances = manhattan_distances(X, Y)
    
    return distances

# Example usage
if __name__ == "__main__":
    # Define vectors X and Y
    X = [[1, 2, 3], [4, 5, 6]]
    Y = [[7, 8, 9], [10, 11, 12]]

    # Compute L1 distances
    distances = compute_l1_distances(X, Y)

    # Print the distances
    print("L1 Distances:")
    print(distances)
