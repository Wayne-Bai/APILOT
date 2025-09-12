
from sklearn.preprocessing import InverseTransformer
import pandas as pd

# load the transformed data
transformed_data = pd.read_csv("transformed_data.csv")

# define the inverse transformer
inverse_transformer = InverseTransformer(transformed_data)

# transform the data back to its original space
original_data = inverse_transformer.fit_transform(transformed_data)
