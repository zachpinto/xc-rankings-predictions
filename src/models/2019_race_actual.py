import pandas as pd

# Load the actual race data
file_path = '../../data/interim/data.csv'  # Update this path to the location of your actual race data file
df = pd.read_csv(file_path)


# Function to calculate race results with points
def calculate_race_results(df, year):
    # Filter the data for the given year
    df_year = df[df['Year'] == year]

    # Sort by time to rank runners
    df_year = df_year.sort_values(by='Time').reset_index(drop=True)

    # Initialize a dictionary to track the number of runners per school
    runner_count = {school: 0 for school in df_year['School'].unique()}

    # Initialize a list to store points
    points = []

    # Iterate through the sorted dataframe and assign points
    current_points = 1
    for index, row in df_year.iterrows():
        school = row['School']
        if runner_count[school] < 7:
            points.append(current_points)
            current_points += 1
        else:
            points.append(None)
        runner_count[school] += 1

    df_year['Points'] = points

    # Select the required columns
    race_results = df_year[['School', 'Name', 'Time', 'Points']]
    race_results.rename(columns={'Name': 'Runner'}, inplace=True)

    return race_results


# Calculate race actuals for 2018 and 2019
race_actuals_2019 = calculate_race_results(df, 2019)

# Save the race actuals to new CSV files
race_actuals_2019.to_csv('../../reports/2019_race_actual.csv', index=False)

print("2019 race actual was saved.")
