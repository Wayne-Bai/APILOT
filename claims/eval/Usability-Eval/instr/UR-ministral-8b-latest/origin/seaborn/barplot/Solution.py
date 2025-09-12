import seaborn as sns
import matplotlib.pyplot as plt

# Example data
data = sns.load_dataset("iris")

# Assuming you have point estimates and confidence intervals
point_estimates = data['sepal_length'].mean()
confidence_interval = 1.96 * data['sepal_length'].std() / data['sepal_length'].count() ** 0.5

# Create a bar
plt.barh(0, point_estimates, xerr=[-confidence_interval, confidence_interval], height=0.5, capsize=5)

# Customize the bar
plt.xlabel('Sepal Length (cm)')
plt.ylabel('')
plt.title('Point Estimate and Confidence Interval of Sepal Length')
plt.show()
