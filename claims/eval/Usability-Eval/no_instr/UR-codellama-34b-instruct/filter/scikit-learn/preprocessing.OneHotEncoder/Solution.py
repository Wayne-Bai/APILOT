
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Load data
data = pd.read_csv('data.csv')

# Encode categorical features as one-hot
enc = OneHotEncoder(handle_unknown='ignore', sparse=False)
encoded_data = enc.fit_transform(data[['categorical_feature']])
