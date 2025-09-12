from sklearn.preprocessing import OneHotEncoder

# Assume 'df' is the DataFrame and 'categorical_column' is the column we want to encode

# Step 1: Apply One-Hot encoding to the categorical column
one_hot = pd.get_dummies(df[[categorical_column]])

# Step 2: As we only have one categorical column here, if there were more columns we would:
# one_hot = OneHotEncoder().fit_transform(df[['categorical_column_1', 'categorical_column_2']]).toarray()

# Step 3: Before concatenating, we need to convert the one-hot encoding result to a DataFrame which is what we want but not yet
one_hot = pd.DataFrame(one_hot)

# Step 4: Finally, we concatenate our DataFrame with the one-hot array we made
df = pd.concat([df, one_hot], axis=1)

# Now, check your DataFrame
df
