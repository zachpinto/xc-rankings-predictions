import pandas as pd
import re

# Load the CSV file
file_path = '../../data/raw/2013.csv'  # Path to your CSV file
df = pd.read_csv(file_path, header=None, encoding='utf-8')


# Define a function to parse each row and extract the needed information
def parse_row_v6(row):
    # Remove non-breaking spaces and other unwanted characters
    row = row.replace('\xa0', ' ').replace('&nbsp;', ' ')

    # Regex pattern to match the required parts, including handling trailing numbers, dashes, apostrophes, and varied grade levels
    pattern = r'^\s*\d+\s+([\w\', ]+?)\s+(SR|Sr|JR|Jr|SO|So|FR|Fr|\d{1,2})\s+([A-Za-z -]+?)\s+(\d{1,2}:\d{2}\.\d{2})'
    match = re.match(pattern, row)
    if match:
        name = match.group(1).strip()
        grade = match.group(2).strip()
        school = match.group(3).strip()
        time = match.group(4).strip()
        return pd.Series([name, grade, school, time])
    else:
        # If pattern does not match, return None for each column to filter out later
        return pd.Series([None, None, None, None])


# Apply the function to each row of the dataframe
parsed_df_v6 = df[0].apply(parse_row_v6)

# Rename the columns
parsed_df_v6.columns = ['Name', 'Grade', 'School', 'Time']

# Remove rows with None in 'Name'
parsed_df_v6 = parsed_df_v6.dropna(subset=['Name'])

# Save the cleaned dataframe to a new CSV file
output_file_path = '../../data/interim/2013.csv'  # Path to save the cleaned file
parsed_df_v6.to_csv(output_file_path, index=False, encoding='utf-8')

print("Data cleaning and transformation complete. The cleaned file is saved at:", output_file_path)
