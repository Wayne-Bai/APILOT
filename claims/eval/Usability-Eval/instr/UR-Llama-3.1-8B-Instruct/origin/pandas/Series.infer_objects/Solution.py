# Import necessary libraries
import pandas as pd
from pandas.api.types import is_numeric_dtype
from IPython.display import display

# Create a sample DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'Country': ['USA', 'UK', 'Australia', 'Germany'],
    'Score': ['90', '85', '95', '92']
}
df = pd.DataFrame(data)

# Print the initial DataFrame
print("Initial DataFrame:")
display(df)

# Check the dtypes of each column
print("\nData Types:")
print(df.dtypes)

# Attempt to infer better dtypes for object columns
# First, exclude numeric columns
object_cols = [col for col in df.columns if not is_numeric_dtype(df[col])]

# Use anomalies() function from pandas.api.types to get most common and second most common values for each object column
for col in object_cols:
    anomalies = pd.api.types.an_ObjectArenaType_values(df[col])
    most_common, second_most_common = anomalies.nlargest(2)
    
    # If the ratio of the second most common value to the most common value is less than 0.1, 
    # then it's likely a categorical column
    if anomalies.size > 0 and anomalies[most_common] / anomalies[second_most_common] < 0.1:
        print(f"\nInferred dtype for column '{col}': category (categorical column)")
        df[col] = pd.Categorical(df[col]).codes  # Convert to categorical codes
    else:
        print(f"Inferred dtype for column '{col}': object")  # Leave it as object for now
