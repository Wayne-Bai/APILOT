import pandas as pd

# Assuming df is your DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Apply Styler to DataFrame
styler = df.style

# Write Styler to a buffer
buffer = styler.render()

# Write buffer to a file (e.g., html)
with open('styled_table.html', 'w') as f:
    f.write(buffer)
