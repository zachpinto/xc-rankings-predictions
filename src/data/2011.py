import pandas as pd
import re

# Load the new CSV file
file_path = "../../data/raw/2011.csv"
df = pd.read_csv(file_path)

# Define a function to parse each row and extract the needed information
def parse_row_v6(row):
    # Regex
    pattern = r'^\d+ ([\w\', ]+?) (\d{1,2}|SR|Sr|JR|Jr|SO|So|FR|Fr) ([\w -]+?) (\d{1,2}:\d{2}\.\d{2})'
    match = re.match(pattern, row)
    if match:
        name = match.group(1).strip()
        grade = match.group(2).strip()
        school = match.group(3).strip()
        time = match.group(4).strip()
        return pd.Series([name, grade, school, time])
    else:
        # If pattern does not match, return the original row as the 'Name'
        return pd.Series([row, None, None, None])

# Apply the function to each row of the dataframe
parsed_df_v6 = df.iloc[:, 0].apply(parse_row_v6)

# Rename the columns
parsed_df_v6.columns = ['Name', 'Grade', 'School', 'Time']

# Remove rows with None in 'Name'
parsed_df_v6 = parsed_df_v6[parsed_df_v6['Name'].notna()]

# Save the cleaned dataframe to a new CSV file
output_file_path = "../../data/interim/2011.csv"
parsed_df_v6.to_csv(output_file_path, index=False)

print("Data cleaning and transformation complete. The cleaned file is saved at:", output_file_path)
