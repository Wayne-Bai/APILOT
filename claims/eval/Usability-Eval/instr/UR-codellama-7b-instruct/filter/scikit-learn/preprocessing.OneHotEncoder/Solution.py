
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Load the data
df = pd.read_csv('data.csv')

# Encode categorical features as a one-hot numeric array
enc = OneHotEncoder(sparse=False, categories='auto')
X = enc.fit_transform(df[['category1', 'category2']])
