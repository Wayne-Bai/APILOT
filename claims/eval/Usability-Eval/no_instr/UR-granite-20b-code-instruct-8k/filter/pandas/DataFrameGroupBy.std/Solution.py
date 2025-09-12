import pandas as pd

# Assuming you have a DataFrame named df with columns 'group' and 'value'
# Replace 'value' with the actual column name containing the values you want to compute the standard deviation for

df_clean = df.dropna(subset=['value'])  # Drop rows with missing values in the 'value' column

grouped_df = df_clean.groupby('group')['value']  # Group the DataFrame by the 'group' column and select the 'value' column

std_dev = grouped_df.std()  # Compute the standard deviation for each group

print(std_dev)  # Output the standard deviation for each group
