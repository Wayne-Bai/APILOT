import seaborn as sns
import matplotlib.pyplot as plt

# Generating a larger dataset
data = sns.load_dataset('diamonds')

# Creating an enhanced box plot for the 'price' variable
plt.figure(figsize=(12, 6))
sns.boxenplot(x='cut', y='price', data=data)

plt.title('Enhanced Box Plot of Diamond Prices by Cut Quality')
plt.xlabel('Cut Quality')
plt.ylabel('Price')
plt.show()
