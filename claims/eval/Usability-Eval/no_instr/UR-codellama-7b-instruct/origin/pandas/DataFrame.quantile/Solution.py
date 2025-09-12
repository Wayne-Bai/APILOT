
import pandas as pd

# Define the data frame and the quantile range
df = pd.read_csv("data.csv")
quantiles = [0, 0.25, 0.5, 0.75, 1]

# Use the describe method to calculate the quantiles for each axis
describe = df.describe(quantiles=quantiles)

# Extract the values at the given quantile over requested axis and print them
for quant in quantiles:
    value = describe.loc[quant, :]
    print(f"Quantile {quant}: {value}")
