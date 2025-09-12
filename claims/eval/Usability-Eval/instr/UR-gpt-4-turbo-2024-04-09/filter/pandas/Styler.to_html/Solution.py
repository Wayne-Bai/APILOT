import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'Score': [88, 92, 95]}
df = pd.DataFrame(data)

# Create a Styler object using any styling functions you prefer
styler = df.style.applymap(lambda x: 'color: red' if isinstance(x, int) and x > 90 else 'color: black')

# Write Styler to a file
with open('mystyle.html', 'w') as f:
    f.write(styler.render())
