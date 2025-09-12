import pandas as pd

# Sample data
data = {
    'sales': [100, 150, 200, 250, 300, 350, 400]
}

# Create DataFrame
df = pd.DataFrame(data)

# Calculate rolling window statistics
# Using a window size of 3
rolling_result = df['sales'].rolling(window=3).mean()

# Display the result
print(rolling_result)
