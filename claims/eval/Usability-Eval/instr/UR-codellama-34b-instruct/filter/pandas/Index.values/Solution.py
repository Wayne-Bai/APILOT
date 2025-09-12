
import pandas as pd

# create a sample DataFrame
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# create an Index from the DataFrame
index = df.index

# output the data in the Index as a numpy array
print(np.array(index))
