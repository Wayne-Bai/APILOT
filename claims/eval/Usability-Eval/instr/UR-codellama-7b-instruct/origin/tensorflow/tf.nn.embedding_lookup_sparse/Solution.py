
import tensorflow as tf

# Define the list of tensors
tensors = [tf.constant([[1, 2], [3, 4]]), tf.constant([[5, 6], [7, 8]])]

# Define the ids and weights for lookups
ids = [[0, 1], [2, 3]]
weights = [0.5, 1.0]

# Create a lookup function that takes an id and weight as inputs
def lookup(id, weight):
    # Lookup the embedding tensor from the list of tensors using the id
    embedding = tf.gather(tensors, id)
    
    # Multiply the embedding by the weight
    return embedding * weight

# Apply the lookup function to each id-weight pair
results = [lookup(id, weight) for id, weight in zip(ids, weights)]

# Print the results
print(results)
