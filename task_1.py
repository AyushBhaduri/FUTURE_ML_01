import pandas as pd

# Load the data
df = pd.read_csv('train.csv')

# Convert the 'date' column to datetime objects
df['date'] = pd.to_datetime(df['date'])

# Look at the first few rows
print(df.head())

# Check the column names to make sure we have 'date' and 'sales'
print(df.columns)