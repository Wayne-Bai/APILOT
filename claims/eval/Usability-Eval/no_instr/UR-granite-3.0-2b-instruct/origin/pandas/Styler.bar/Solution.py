import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have a DataFrame `df` with columns 'Date', 'Open', 'High', 'Low', 'Close'

# Set 'Date' as the index
df.set_index('Date', inplace=True)

# Plot the bar chart
plt.bar(df.index, df['Open'], color='blue', label='Open')
plt.bar(df.index, df['High'], color='green', label='High', bottom=df['Open'])
plt.bar(df.index, df['Low'], color='red', label='Low', bottom=df['High'])
plt.bar(df.index, df['Close'], color='black', label='Close', bottom=df['Low'])

# Add title, labels, and legend
plt.title('Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Show the plot
plt.show()
