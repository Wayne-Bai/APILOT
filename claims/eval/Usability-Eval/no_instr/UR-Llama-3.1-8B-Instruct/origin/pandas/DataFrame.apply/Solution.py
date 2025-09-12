# Import the pandas library
import pandas as pd

# Create a sample DataFrame
data = {
    "Name": ["Tom", "Nick", "John", "Tom", "John"],
    "Age": [20, 21, 19, 20, 18]
}
df = pd.DataFrame(data)

# Define a function to calculate the mean age
def calculate_mean_age(group):
    return group["Age"].mean()

# Apply the function along the 'Name' axis
result = df.groupby("Name")["Age"].apply(calculate_mean_age)

print(result)
