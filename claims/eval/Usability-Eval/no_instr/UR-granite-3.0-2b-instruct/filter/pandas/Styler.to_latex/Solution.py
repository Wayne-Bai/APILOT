import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Create a Styler object
styler = df.style

# Write Styler to a buffer in LaTeX format
buffer = styler.render()

# Print the buffer
print(buffer)
