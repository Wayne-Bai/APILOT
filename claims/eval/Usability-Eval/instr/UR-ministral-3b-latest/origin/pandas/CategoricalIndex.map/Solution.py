import pandas as pd

# Sample data
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'City': ['New York', 'Paris', 'London', 'Berlin']}

# Create DataFrame
df = pd.DataFrame(data)

# Define the mapping
def new_city(city):
    mapping = {
        'New York': 'NY',
        'Paris': 'FR',
        'London': 'UK',
        'Berlin': 'DE'
    }
    return mapping.get(city, city.lower())

# Apply the mapping function
df['City'] = df['City'].apply(new_city)
