import pandas as pd
import re

# Load the new CSV file
file_path = '../../data/raw/2019.csv'  # Update this path to the location of your file
df = pd.read_csv(file_path, header=None, encoding='utf-8')


# Define a function to parse each row and extract the needed information
def parse_row(row):
    # Convert the row to a single string and clean it
    row_str = ' '.join([str(x) for x in row if pd.notna(x)])
    row_str = row_str.replace('\xa0', ' ').replace('&nbsp;', ' ').strip()

    # Split the row by whitespace
    parts = row_str.split()

    if len(parts) >= 9:
        rank = parts[0]
        name = f"{parts[1]} {parts[2]}"
        grade = parts[3]
        school = ' '.join(parts[4:-3]).strip()
        time = parts[-3]
        return pd.Series([name, grade, school, time])
    else:
        return pd.Series([None, None, None, None])


# Apply the function to each row of the dataframe
parsed_df = df.apply(lambda row: parse_row(row), axis=1)

# Rename the columns
parsed_df.columns = ['Name', 'Grade', 'School', 'Time']

# Remove rows with None in 'Name'
parsed_df = parsed_df.dropna(subset=['Name'])

# Save the cleaned dataframe to a new CSV file
output_file_path = '../../data/interim/2019.csv'  # Update this path to where you want to save the file
parsed_df.to_csv(output_file_path, index=False, encoding='utf-8')

print("Data cleaning and transformation complete. The cleaned file is saved at:", output_file_path)
