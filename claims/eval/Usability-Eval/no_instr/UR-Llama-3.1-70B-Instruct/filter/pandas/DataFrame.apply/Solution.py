# Importing the pandas library
import pandas as pd

# Creating a DataFrame
data = {
  "Name": ["Tom", "Nick", "krish", "Jack"],
  "Age": [20, 21, 19, 18],
  "Score": [90, 85, 88, 92]
}
df = pd.DataFrame(data)

# Print the original DataFrame
print("Original DataFrame:")
print(df)

# Define a function to calculate the grade based on the score
def calculate_grade(score):
  if score >= 90:
    return "A"
  elif score >= 80:
    return "B"
  else:
    return "C"

# Apply the function to the 'Score' column along axis=0 (default)
df['Grade'] = df['Score'].apply(calculate_grade)

# Print the DataFrame after applying the function
print("\nDataFrame after applying the function:")
print(df)
