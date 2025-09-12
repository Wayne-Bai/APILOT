
import pandas as pd

# read data into a DataFrame
df = pd.read_csv("data.csv")

# drop rows with missing values in any column
df.dropna(inplace=True)

# display the resulting DataFrame
print(df)
