import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Tom', 'Nick', 'John'],
    'Age': [20, 21, 19],
    'Score': [90, 85, 88]
}
df = pd.DataFrame(data)

# Create another sample DataFrame
data1 = {
    'Name': ['Tom', 'Nick', 'John'],
    'Age': [20, 21, 19],
    'Score': [90, 85, 88]
}
df1 = pd.DataFrame(data1)

# Test if two DataFrames are equal with additional check_like argument
try:
    pd.testing.assert_series_equal(df['Name'], df1['Name'], check_like=True)
    print("Series 'Name' are equal.")
except AssertionError as e:
    print(f"Series 'Name' are not equal: {e}")

try:
    pd.testing.assert_series_equal(df['Age'], df1['Age'], check_like=True)
    print("Series 'Age' are equal.")
except AssertionError as e:
    print(f"Series 'Age' are not equal: {e}")

try:
    pd.testing.assert_series_equal(df['Score'], df1['Score'], check_like=True)
    print("Series 'Score' are equal.")
except AssertionError as e:
    print(f"Series 'Score' are not equal: {e}")

print("DataFrames are equal.")
try:
    pd.testing.assert_frame_equal(df, df1, check_like=True)
except AssertionError as e:
    print(f"DataFrames are not equal: {e}")
