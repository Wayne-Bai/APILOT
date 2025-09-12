
import pandas as pd

# create a sample dataframe
data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
df = pd.DataFrame(data)

# hide column headers
df_html = df.to_html(index=False)
print(df_html)
