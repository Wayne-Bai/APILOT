
import pandas as pd

# Creating a dataframe with sample data
data = {
    'Name': ['John', 'Alice', 'Bob', 'Mike'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'London', 'Paris', 'Madrid']
}
df = pd.DataFrame(data)

# Hide the entire index
df.style.hide_index()

# Hiding specific keys from the index
df.style.format({'Name': lambda x: ''})
