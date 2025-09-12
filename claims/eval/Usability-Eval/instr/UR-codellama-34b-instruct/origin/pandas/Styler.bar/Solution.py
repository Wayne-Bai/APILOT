
import pandas as pd
import plotly.graph_objects as go

# create a sample dataset
data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
df = pd.DataFrame(data)

# define the color palette for the bars
color_palette = ['red', 'green', 'blue']

# create a figure object with plotly
fig = go.Figure()

# add a bar trace for each column in the dataset
for i, col in enumerate(df.columns):
    fig.add_trace(go.Bar(x=list(df[col]), y=[0, 1, 2], name=col, color=color_palette[i]))

# set the bar mode to 'stack' to stack the bars on top of each other
fig.update_layout(barmode='stack')

# add a title and labels for the chart
fig.update_layout(title='Bar Chart in Cell Backgrounds', xaxis_title='Values', yaxis_title='Cells')

# show the figure
fig.show()
