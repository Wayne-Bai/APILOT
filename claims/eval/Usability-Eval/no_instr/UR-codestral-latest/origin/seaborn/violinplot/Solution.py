# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt

# Load example dataset
tip = sns.load_dataset("tips")

# Create a figure and a set of subplots
fig, ax = plt.subplots()

# Draw the density plot
sns.kdeplot(tip["total_bill"], ax=ax, color="red", fill=True)

# Add boxplot statistics, note that we should match the ax parameter to the same axis.
sns.boxplot(x=tip["total_bill"], ax=ax, color="blue", whiskerprops={'color':'blue'},
            capprops={'color':'blue'}, boxprops={'color':'blue', 'facecolor':'none'})

# Show the plot
plt.show()
