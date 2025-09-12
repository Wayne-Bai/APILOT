# Sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Define a function to apply
def multiply_data(input_data):
    return input_data * 2

# Apply the function to the entire DataFrame
result_df = df.apply(multiply_data)

print(result_df)
