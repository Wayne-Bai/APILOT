import pandas as pd

# Assume we have a DataFrame with two columns: 'Name' and 'Age'
data = {
    'Name': ['Tom', 'Nick', 'John', 'Patrick'],
    'Age': [20, 21, 19, 22]
}
df = pd.DataFrame(data)

# Now, let's assume we have a function that gives us the ethnicity based on the age
def get_ethnicity(age):
    if age < 20:
        return 'Youth'
    elif age < 40:
        return 'Adult'
    else:
        return 'Senior'

# We can use the map() function to apply this function to the 'Age' column
# map() is a pandas method that applies a function to each element in a Series
df['Ethnicity'] = df['Age'].map(get_ethnicity)

print(df)
