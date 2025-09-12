
import pandas as pd

# Load data from a file or dataset
data = pd.read_csv("data.csv")

# Drop rows with missing values
data.dropna(inplace=True)

# Group the data by a categorical variable and compute mean of continuous variable
means = data.groupby("category").mean()["continuous"]

# Compute standard error of the mean for each group
std_errors = means.sem()
