
import tensorflow as tf

# Load the data
data = pd.read_csv("data.csv")

# Create a dictionary mapping the IDs to their corresponding embeddings
id_to_embedding = {int(id): embedding for id, embedding in zip(data["ID"], data["Embedding"])}

# Define a function to perform the lookup embedding
def lookuper(inputs):
    outputs = []
    for input in inputs:
        if int(input) not in id_to_embedding:
            outputs.append([0] * 10)
        else:
            outputs.append(id_to_embedding[int(input)])
    return tf.convert_to_tensor(outputs, dtype=tf.float32)

# Define the input and output tensors for the lookup embedding
inputs = tf.constant(data["ID"])
outputs = lookuper(inputs)
