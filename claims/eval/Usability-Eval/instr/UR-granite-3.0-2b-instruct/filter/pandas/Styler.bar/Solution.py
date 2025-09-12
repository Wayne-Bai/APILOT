import pandas as pd
import matplotlib.pyplot as plt

# Assuming df is your DataFrame and 'column1' and 'column2' are the columns you want to plot
df = pd.DataFrame({
    'column1': [1, 2, 3, 4, 5],
    'column2': [2, 3, 2, 5, 3]
})

plt.bar(df['column1'], df['column2'])
plt.xlabel('Column 1')
plt.ylabel('Column 2')
plt.title('Bar Chart')
plt.show()
