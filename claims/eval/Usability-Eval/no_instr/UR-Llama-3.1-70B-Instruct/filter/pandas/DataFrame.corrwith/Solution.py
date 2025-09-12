# Import pandas library
import pandas as pd
import numpy as np

# Create a DataFrame
data = np.random.rand(10, 5)
df = pd.DataFrame(data, columns=['A', 'B', 'C', 'D', 'E'])

# Compute pairwise correlation
pairwise_corr = df.corr()

print(pairwise_corr)
