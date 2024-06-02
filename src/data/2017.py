import pandas as pd
import csv

# Load the CSV file
file_path = '../../data/raw/2017.csv'  # Update this path to the location of your file
df = pd.read_csv(file_path, skiprows=1, header=None, encoding='utf-8')

# Define the column names
df.columns = ['Place', 'LastName', 'FirstName', 'Grade', 'School', 'Time']

# Remove the leading numbers (places) column
df = df.drop(columns=['Place'])

# Combine the last and first names with proper formatting
df['Name'] = df.apply(lambda row: f'{row["LastName"].strip()} {row["FirstName"].strip()}', axis=1)

# Add quotes around the combined name without extra quotes
df['Name'] = df['Name'].apply(lambda x: f'"{x}"')

# Reorder the columns
df = df[['Name', 'Grade', 'School', 'Time']]

# Sort the dataframe by Time in ascending order
df = df.sort_values(by='Time')

# Save the cleaned and sorted dataframe to a new CSV file
output_file_path = '../../data/interim/2017.csv'  # Update this path to where you want to save the file
df.to_csv(output_file_path, index=False, encoding='utf-8', quoting=csv.QUOTE_MINIMAL)

print("Data cleaning and sorting complete. The cleaned file is saved at:", output_file_path)
