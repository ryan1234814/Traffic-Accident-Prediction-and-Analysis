import pandas as pd

# Load the dataset
df = pd.read_csv('traffic_data.csv')

# Display the first few rows
print("First 5 rows of the dataset:")
print(df.head())
print("\n" + "="*50 + "\n")

# Display column names and their data types
print("Column names and data types:")
print(df.info())
print("\n" + "="*50 + "\n")

# Display the count of missing values for each column
print("Missing values per column:")
print(df.isnull().sum())
print("\n" + "="*50 + "\n")

# Display basic descriptive statistics for numerical columns
print("Descriptive statistics for numerical columns:")
print(df.describe())
