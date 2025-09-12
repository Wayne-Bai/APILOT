import pandas as pd

# Assuming data is a dictionary containing the data for the DataFrame
df = pd.DataFrame(data, columns=pd.MultiIndex.from_tuples(data.keys()))
