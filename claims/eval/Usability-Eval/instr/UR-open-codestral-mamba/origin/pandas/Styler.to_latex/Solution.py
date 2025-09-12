import pandas as pd

# Sample dataframe
df = pd.DataFrame({
   'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
   'B': ['one', 'one', 'two', 'two', 'one', 'one'],
   'C': ['small', 'large', 'large', 'small', 'small', 'large'],
   'D': [1, 2, 2, 3, 3, 4],
   'E': [2, 4, 5, 5, 6, 6],
})

# Writing dataframe to a LaTeX formatted string
df_latex = df.to_latex(index=False)

# Write to a file
with open('output.tex', 'w') as file:
    file.write(df_latex)

# Or, write to a buffer
buffer = StringIO()
df.to_latex(buffer, index=False)
buffer.getvalue()

