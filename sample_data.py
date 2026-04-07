import pandas as pd

# Load the health data CSV file
file_path = 'data/health_data.csv'
data = pd.read_csv(file_path)

# Print the first 5 rows of the dataframe
print("First 5 rows of the dataframe:")
print(data.head())

# Calculate and print the number of missing values in each column
missing_values = data.isnull().sum()
print("\nNumber of missing values in each column:")
print(missing_values)