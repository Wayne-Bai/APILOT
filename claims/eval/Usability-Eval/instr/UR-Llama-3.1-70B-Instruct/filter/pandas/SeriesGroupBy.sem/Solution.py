import pandas as pd
import numpy as np

# Creating a sample dataframe with grouped data
np.random.seed(0)
data = {
    'Group': np.repeat(['A', 'B', 'C'], 10),
    'Value': np.random.randn(30)
}
df = pd.DataFrame(data)

# Introducing some missing values
df.loc[df.sample(frac=0.1).index, 'Value'] = np.nan

# Computing standard error of the mean of groups
sem = df.groupby('Group')['Value'].apply(lambda x: x.std() / np.sqrt(x.count()))

print(sem)
