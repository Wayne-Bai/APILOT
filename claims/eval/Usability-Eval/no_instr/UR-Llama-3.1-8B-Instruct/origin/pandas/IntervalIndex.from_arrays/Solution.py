
import pandas as pd

# Creating two arrays defining the left and right bounds
left_bounds = [1, 3, 5, 7, 9]
right_bounds = [3, 6, 7, 8, 10]

# Creating a DataFrame to represent the intervals
intervals = pd.DataFrame({
    'left': left_bounds,
    'right': right_bounds
})

# Display the DataFrame
print(intervals)
