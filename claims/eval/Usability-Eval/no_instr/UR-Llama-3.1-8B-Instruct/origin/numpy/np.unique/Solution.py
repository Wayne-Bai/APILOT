import numpy as np

# Function to find unique elements of an array
def find_unique_elements(arr):
    # Use np.unique() function to find unique elements
    # and return only > 1 to find elements repeated more than twice.
    unique = np.unique(arr[np.unique(arr, return_index=True)[1] < 2], return_index=True, return_counts=True)
    
    # Print the unique elements
    print("Unique elements: ", unique[0])

    # Print the count of each unique element
    print("Count of each unique element: ", unique[2])

    # Function to print the start and end index of each unique element
    def print_start_end_idx(arr):
        seen = []
        for num in arr:
            if num not in seen:
                seen.append(num)
                print(f"Start and end index of {num}: [{np.where(arr==num)[0][0]}, {np.where(arr==num)[0][-1]})]")

    # Print the start and end index of each unique element
    print_start_end_idx(arr)

# Test the function
arr = np.array([1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5])

find_unique_elements(arr)
