import pandas as pd

# create sample data
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

# set background color for the bar chart
background_color = '#d9edf7'

# create a bar chart using the background_color
fig, ax = plt.subplots()
ax.bar(df['A'], df['B'], width=0.5, bottom=0, color='black')
ax.set_facecolor(background_color)
plt.show()
