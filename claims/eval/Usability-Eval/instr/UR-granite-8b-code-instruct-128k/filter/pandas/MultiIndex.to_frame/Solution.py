import pandas as pd

# Assuming 'df' is the DataFrame you want to convert to a MultiIndex DataFrame
multi_index_df = pd.DataFrame(df.index.levels[0], columns=['Level_0'])
multi_index_df['Level_1'] = df.index.levels[1]
multi_index_df['Level_2'] = df.index.levels[2]
