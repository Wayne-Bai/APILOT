from sklearn.preprocessing import OneHotEncoder

# Example dataframe
data = pd.DataFrame({
    'color': ['red', 'green', 'blue', 'red', 'green'],
    'shape': ['circle', 'square', 'circle', 'square', 'triangle']
})

# Initialize the OneHotEncoder
encoder = OneHotEncoder()

# Fit and transform the data
encoded_data = encoder.fit_transform(data)

# Convert the array to a dataframe for better readability
encoded_df = pd.DataFrame(encoded_data.toarray(), columns=encoder.get_feature_names_out(data.columns))

print(encoded_df)
