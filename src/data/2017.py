import pandas as pd

# Load the CSV file
file_path = '../../data/raw/2017.csv'
df = pd.read_csv(file_path, header=None)


# Function to extract relevant information from each row
def extract_relevant_info(row):
    name = f"{row[2].strip()}{row[3].strip()}"
    grade = row[4]
    school = row[5].strip() if not pd.isna(row[5]) else ''

    # Locate the time value, which should always be in the format of 'MM:SS.d'
    time = ''
    for value in row[6:]:
        if isinstance(value, str) and ':' in value:
            time = value.strip()
            break

    # Combine school if there are multiple words
    school_parts = []
    for value in row[5:]:
        if isinstance(value, str) and not (':' in value):
            school_parts.append(value.strip())
        if ':' in value:
            break
    school = ' '.join(school_parts)

    return [name, grade, school, time]


# Apply the function to each row
processed_data = df.apply(extract_relevant_info, axis=1)
processed_df = pd.DataFrame(processed_data.tolist(), columns=['Name', 'Grade', 'School', 'Time'])

# Save the cleaned data to a new CSV file
output_file_path = '../../data/interim/2017.csv'
processed_df.to_csv(output_file_path, index=False)

# Display the processed data for verification
print(processed_df.head())
