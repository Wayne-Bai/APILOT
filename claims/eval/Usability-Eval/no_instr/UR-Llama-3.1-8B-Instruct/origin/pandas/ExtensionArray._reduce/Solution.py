import pandas as pd

def reduction_operation():
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda', 'Kitty'],
            'Age': [28, 24, 35, 32, 40]}
    
    df = pd.DataFrame(data)
    
    # Use the min function to get the minimum age
    min_age = df['Age'].min()
    print(f'The minimum age is: {min_age}')

    # Use the max function to get the maximum age
    max_age = df['Age'].max()
    print(f'The maximum age is: {max_age}')

    # Use the mean function to get the average age
    average_age = df['Age'].mean()
    print(f'The average age is: {average_age}')

    # Use the sum function to get the total age
    total_age = df['Age'].sum()
    print(f'The total age is: {total_age}')

    # Use the median function to get the middle value
    median_age = df['Age'].median()
    print(f'The median age is: {median_age}')

reduction_operation()
