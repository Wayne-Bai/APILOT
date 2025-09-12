# Import the pandas library
import pandas as pd

# Import the matplotlib library for visualization
import matplotlib.pyplot as plt

# Assuming you have a DataFrame df with your data
# Here, I am creating a sample DataFrame for the demonstration
data = {'Name': ['Tom', 'Nick', 'John', 'Jessica'],
        'Age': [20, 21, 19, 18]}
df = pd.DataFrame(data)

# Draw bar chart
plt.bar(df['Name'], df['Age'], color ='maroon', width = 0.4)

plt.xlabel("Name")
plt.ylabel("Age")
plt.title("Bar Chart of Age")
plt.show()
