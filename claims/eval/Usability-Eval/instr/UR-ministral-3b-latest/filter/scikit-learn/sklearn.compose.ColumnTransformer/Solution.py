import pandas as pd
from numpy import array
import tensorflow as tf
from sklearn.preprocessing import transformers

# Example usage:
data = array([[5.1, 3.5, 1.4, 0.2],
              [4.9, 3.0, 1.4, 0.2],
              [4.7, 3.2, 1.3, 0.2],
              [4.6, 3.1, 1.5, 0.2],
              [5.0, 3.6, 1.4, 0.2]])

# Reshaping to 2D axis to be used with transformers
data = data.reshape(-1, 1)

# Convert to pandas DataFrame
df = pd.DataFrame(data, columns=['Feature1'])

# Define the transform that will be applied to the DataFrame
def example_transform(df):
    inputs_tensor = tf.convert_to_tensor(df, dtype=tf.float32)
    hidden_input = tf.Variable(inputs_tensor, trainable=False)
    outputs_tensor = tf.nn.relu(hidden_input)
    return outputs_tensor

# Apply the transform
df['Feature1_transformed'] = example_transform(df)['Feature1']

print(df)
